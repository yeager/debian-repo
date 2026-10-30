#!/usr/bin/env python3
"""Validate the pinned GitHub release assets used by the APT import workflow."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "maintenance/release-assets.json"
REPO_RE = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
TAG_RE = re.compile(r"[A-Za-z0-9._-]+\Z")
NAME_RE = re.compile(r"[A-Za-z0-9._+~-]+\.deb\Z")
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")


def fail(message):
    print(f"{MANIFEST.relative_to(ROOT)}: {message}", file=sys.stderr)
    raise SystemExit(1)


try:
    assets = json.loads(MANIFEST.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as error:
    fail(f"cannot read valid JSON: {error}")

if not isinstance(assets, list) or not assets:
    fail("expected a non-empty JSON array")

seen = set()
for index, asset in enumerate(assets):
    prefix = f"entry {index + 1}"
    if not isinstance(asset, dict):
        fail(f"{prefix} must be an object")
    required = {"repo", "tag", "name", "size", "url", "sha256"}
    if not required.issubset(asset):
        fail(f"{prefix} is missing fields: {', '.join(sorted(required - asset.keys()))}")
    if not isinstance(asset["repo"], str) or not REPO_RE.fullmatch(asset["repo"]):
        fail(f"{prefix} has an invalid repository")
    if not isinstance(asset["tag"], str) or not TAG_RE.fullmatch(asset["tag"]):
        fail(f"{prefix} has an invalid release tag")
    if not isinstance(asset["name"], str) or not NAME_RE.fullmatch(asset["name"]):
        fail(f"{prefix} has an unsafe DEB filename")
    if type(asset["size"]) is not int or asset["size"] <= 0:
        fail(f"{prefix} size must be a positive integer")
    expected_url = f"https://github.com/{asset['repo']}/releases/download/{asset['tag']}/{asset['name']}"
    if asset["url"] != expected_url or urlparse(asset["url"]).hostname != "github.com":
        fail(f"{prefix} URL does not match its repository, tag, and filename")
    if not isinstance(asset["sha256"], str) or not SHA256_RE.fullmatch(asset["sha256"]):
        fail(f"{prefix} SHA-256 must contain 64 lowercase hexadecimal characters")
    identity = (asset["repo"].lower(), asset["tag"], asset["name"])
    if identity in seen:
        fail(f"{prefix} duplicates a repository/tag/filename entry")
    seen.add(identity)

print(f"Validated {len(assets)} pinned DEB release assets")
