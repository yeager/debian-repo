# Nylander L10n Suite, Debian Repository

Debian and Ubuntu packages published via GitHub Pages.

The repository contains packages including:
- ANPR Viewer
- Apt Changelog Viewer
- PaintBrush
- Signal Lantern
- and other localization/development tools

## Setup

```bash
wget -qO /tmp/yeager-repo-key.asc https://yeager.github.io/debian-repo/yeager-repo-key.asc
sudo install -m 0644 /tmp/yeager-repo-key.asc /usr/share/keyrings/yeager-repo.asc
echo 'deb [signed-by=/usr/share/keyrings/yeager-repo.asc] https://yeager.github.io/debian-repo ./' | sudo tee /etc/apt/sources.list.d/yeager.list
sudo apt update
```

## Install Signal Lantern

```bash
sudo apt install signal-lantern
```

## Notes

- Repository URL: <https://yeager.github.io/debian-repo>
- Packages index is published as `Packages`, `Packages.gz`, and `Packages.xz`
- `InRelease` and `Release.gpg` are published for signed metadata

## Updated Swedish language tools

The following packages are available for direct download. They are built from
the repaired upstream sources and work on any architecture with Python 3.10+:

| Package | Version | Download |
| --- | --- | --- |
| svlang | 0.2.0-2 | [DEB](https://yeager.github.io/debian-repo/pool/main/s/svlang/svlang_0.2.0-2_all.deb) |
| swedish-tm | 20260918-1 | [DEB](https://yeager.github.io/debian-repo/pool/main/s/swedish-tm/swedish-tm_20260918-1_all.deb) |
| swedish-foss-terminology | 20260918-1 | [DEB](https://yeager.github.io/debian-repo/pool/main/s/swedish-foss-terminology/swedish-foss-terminology_20260918-1_all.deb) |

Install a downloaded package with `sudo apt install ./PACKAGE_FILE.deb`.
The translation memory and terminology data are installed under
`/usr/share/swedish-tm/` and `/usr/share/swedish-foss-terminology/` respectively.
The svlang package includes both lexicons and fixes false unknown-word reports
for words that are absent from the frequency list but present in a lexicon.

These versions are **not yet in the signed APT indexes**. Publication of updated
indexes and repository cleanup awaits the existing signing key
`7CEE83C9C621B18667DD1BFECAED4975DAB053A8`.

Source commits and package SHA-256 checksums are recorded in
[`maintenance/swedish-tools-20260918.json`](maintenance/swedish-tools-20260918.json).
The [shared RPM/DEB build recipe](https://github.com/yeager/rpm-repo/blob/main/packaging/build-swedish-tools.py)
pins and verifies the source files before building both package formats.

## po-translate 1.6.1

[po-translate_1.6.1_all.deb](https://yeager.github.io/debian-repo/pool/main/p/po-translate/po-translate_1.6.1_all.deb)
fixes plural translation and prevents files from being written after a failed
translation request or altered placeholders. It is available for direct
installation with `sudo apt install ./po-translate_1.6.1_all.deb`; adding it to
the signed APT index awaits the existing repository signing key.
