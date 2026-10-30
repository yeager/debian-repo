#!/usr/bin/env python3
"""Import pinned DEB release assets, canonicalize the pool, and rebuild indexes."""
import hashlib, json, re, shutil, subprocess, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = json.loads((ROOT / "maintenance/release-assets.json").read_text())
POOL = ROOT / "pool"
POOL.mkdir(exist_ok=True)

def metadata(path):
    control = subprocess.check_output(["dpkg-deb", "-f", str(path)], text=True)
    fields = {}
    for line in control.splitlines():
        if line[:1].isspace() or ":" not in line:
            continue
        name, value = line.split(":", 1)
        fields[name] = value.strip()
    identity = tuple(fields.get(name, "") for name in ("Package", "Version", "Architecture"))
    if not all(identity) or not re.fullmatch(r"[a-z0-9][a-z0-9+.-]*", identity[0]):
        raise ValueError(f"Invalid DEB control metadata: {path}")
    return identity

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def canonical(path, identity):
    package = identity[0]
    return POOL / "main" / package[0] / package / path.name

# Migrate legacy packages beside indexes into pool so regenerated indexes keep them.
existing = {}
deb_paths = sorted(
    (path for path in ROOT.rglob("*.deb") if ".git" not in path.parts and not path.name.endswith(".download")),
    key=lambda path: (not path.is_relative_to(POOL), str(path)),
)
for path in deb_paths:
    identity = metadata(path)
    old = existing.get(identity)
    target = canonical(path, identity)
    if old:
        if sha256(old) != sha256(path):
            if old.is_relative_to(POOL) and not path.is_relative_to(POOL):
                print(f"Keeping indexed pool package and preserving differing legacy copy: {path}")
                continue
            raise ValueError(f"Conflicting existing DEB {identity}: {old}, {path}")
        if path != old:
            path.unlink()
        continue
    existing[identity] = path
    if path != target:
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and sha256(target) != sha256(path):
            raise ValueError(f"Refusing to replace different package file: {target}")
        if target.exists():
            path.unlink()
        else:
            shutil.move(str(path), str(target))
        existing[identity] = target

for asset in ASSETS:
    name = asset["name"]
    if not re.fullmatch(r"[A-Za-z0-9._+~-]+\.deb", name):
        raise ValueError(f"Unsafe asset filename: {name!r}")
    if not asset["url"].startswith(f"https://github.com/{asset['repo']}/releases/download/"):
        raise ValueError(f"Unexpected release URL: {asset['url']}")
    temp = POOL / (name + ".download")
    request = urllib.request.Request(asset["url"], headers={"User-Agent": "yeager-debian-repo-import/1"})
    with urllib.request.urlopen(request, timeout=180) as response, temp.open("wb") as stream:
        while chunk := response.read(1024 * 1024):
            stream.write(chunk)
    if temp.stat().st_size != asset["size"]:
        raise ValueError(f"Size mismatch for {asset['repo']}:{name}")
    expected_sha256 = asset.get("sha256")
    if expected_sha256 and sha256(temp) != expected_sha256:
        raise ValueError(f"SHA-256 mismatch for {asset['repo']}:{name}")
    identity = metadata(temp)
    old = existing.get(identity)
    if old:
        if sha256(old) != sha256(temp):
            raise ValueError(f"Conflicting release DEB {identity}: {old}")
        temp.unlink()
        continue
    target = canonical(temp, identity)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise ValueError(f"Refusing to overwrite unrelated package file: {target}")
    shutil.move(str(temp), str(target))
    existing[identity] = target

for arch in ("amd64", "arm64"):
    index_dir = ROOT / "dists/stable/main" / f"binary-{arch}"
    index_dir.mkdir(parents=True, exist_ok=True)
    packages = subprocess.check_output(["dpkg-scanpackages", "--multiversion", "--arch", arch, "pool", "/dev/null"], cwd=ROOT, text=True)
    (index_dir / "Packages").write_text(packages)
    with (index_dir / "Packages.gz").open("wb") as output:
        subprocess.run(["gzip", "-n", "-9c", str(index_dir / "Packages")], check=True, stdout=output)
    with (index_dir / "Packages.xz").open("wb") as output:
        subprocess.run(["xz", "-9e", "-c", str(index_dir / "Packages")], check=True, stdout=output)
shutil.rmtree(ROOT / "dists/stable/main/binary-all", ignore_errors=True)
print(f"Imported/verified {len(ASSETS)} release DEBs; indexed {len(existing)} package versions for amd64/arm64")
