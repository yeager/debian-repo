# Nylander L10n Suite, Debian Repository

Debian and Ubuntu packages published via GitHub Pages.

The repository currently contains **108 packages**, including:
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
