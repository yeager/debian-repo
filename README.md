# Nylander L10n Suite, Debian Repository

Debian and Ubuntu packages published via GitHub Pages.

The repository contains packages including:
- ANPR Viewer
- Apt Changelog Viewer
- PaintBrush
- Signal Lantern
- and other localization/development tools

## Setup

Repository metadata now uses the replacement signing key with fingerprint
`C7982569D1DCC5468A072D94D7B45ED27B9EBB63`. <!-- gitleaks:allow --> The previous key is retired. Existing users must install the new key before
running `sudo apt update`.

```bash
wget -qO /tmp/yeager-repo-key.asc https://yeager.github.io/debian-repo/yeager-repo-key.asc
sudo install -m 0644 /tmp/yeager-repo-key.asc /usr/share/keyrings/yeager-repo.asc
echo 'deb [signed-by=/usr/share/keyrings/yeager-repo.asc] https://yeager.github.io/debian-repo stable main' | sudo tee /etc/apt/sources.list.d/yeager.list
sudo apt update
```

If you already use this repository, replace the old key before running
`sudo apt update`:

```bash
wget -qO /tmp/yeager-repo-key.asc https://yeager.github.io/debian-repo/yeager-repo-key.asc
gpg --show-keys --with-fingerprint /tmp/yeager-repo-key.asc
sudo install -m 0644 /tmp/yeager-repo-key.asc /usr/share/keyrings/yeager-repo.asc
sudo apt update
```

## Install Signal Lantern

```bash
sudo apt install signal-lantern
```

## Ubuntu desktop apps

The repository also provides these Ubuntu-focused desktop tools:

| Package | Purpose |
| --- | --- |
| `ubuntu-start` | First-run, hardware, accessibility, network and security guidance |
| `ubuntu-l10n` | Ubuntu and Launchpad translation statistics |
| `wifi-analyzer` | Wi-Fi signal and channel analysis |
| `apt-changelog-viewer` | Installed package changelogs and security references |

Install them together with:

```bash
sudo apt install ubuntu-start ubuntu-l10n wifi-analyzer apt-changelog-viewer
```

## Notes

- Repository URL: <https://yeager.github.io/debian-repo>
- Packages index is published as `Packages`, `Packages.gz`, and `Packages.xz`
- `InRelease` and `Release.gpg` are published for signed metadata

## Svenska språkverktyg

The following packages are available for direct download. They are built from
the repaired upstream sources and work on any architecture with Python 3.10+:

| Package | Version | Download |
| --- | --- | --- |
| svlang | 0.2.0-2 | [DEB](https://yeager.github.io/debian-repo/pool/main/s/svlang/svlang_0.2.0-2_all.deb) |
| swedish-tm | 20260918-1 | [DEB](https://yeager.github.io/debian-repo/pool/main/s/swedish-tm/swedish-tm_20260918-1_all.deb) |
| swedish-foss-terminology | 20260918-1 | [DEB](https://yeager.github.io/debian-repo/pool/main/s/swedish-foss-terminology/swedish-foss-terminology_20260918-1_all.deb) |
| po-translate | 1.6.1 | [DEB](https://yeager.github.io/debian-repo/pool/main/p/po-translate/po-translate_1.6.1_all.deb) |

Install a downloaded package with `sudo apt install ./PACKAGE_FILE.deb`.
The translation memory and terminology data are installed under
`/usr/share/swedish-tm/` and `/usr/share/swedish-foss-terminology/` respectively.
The svlang package includes both lexicons and fixes false unknown-word reports
for words that are absent from the frequency list but present in a lexicon.

Source commits and package SHA-256 checksums are recorded in
[`maintenance/swedish-tools-20260918.json`](maintenance/swedish-tools-20260918.json).
The [shared RPM/DEB build recipe](https://github.com/yeager/rpm-repo/blob/main/packaging/build-swedish-tools.py)
pins and verifies the source files before building both package formats.

`po-translate` 1.6.1 bevarar pluralformer och lämnar katalogen oförändrad när
en översättningstjänst misslyckas eller ändrar platshållare.
