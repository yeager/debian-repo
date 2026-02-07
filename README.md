# Yeager's Debian Repository

APT repository for translation and localization tools.

## Quick Install

```bash
# Add GPG key
curl -fsSL https://yeager.github.io/debian-repo/yeager.gpg | sudo gpg --dearmor -o /usr/share/keyrings/yeager.gpg

# Add repository
echo 'deb [signed-by=/usr/share/keyrings/yeager.gpg] https://yeager.github.io/debian-repo stable main' | sudo tee /etc/apt/sources.list.d/yeager.list

# Update and install
sudo apt update
sudo apt install l10n-lint l10n-lint-gtk po-translate po-diff tp-lint traduco
```

## Available Packages

| Package | Version | Description |
|---------|---------|-------------|
| **l10n-lint** | 1.14.9 | Linter for localization files (.po, .ts) |
| **l10n-lint-gtk** | 1.2.9 | GTK4 graphical interface for l10n-lint |
| **po-translate** | 1.4.0 | Batch translate PO and TS files |
| **po-diff** | 1.0.0 | Compare and diff PO files |
| **tp-lint** | 1.8.0 | Translation Project linter and statistics |
| **traduco** | 0.2.0 | GTK4 translation file editor for PO, TS, and JSON |

## GPG Signing

Repository is signed with GPG key `CAED4975DAB053A8`.

- Public key: [yeager.gpg](yeager.gpg)
- Fingerprint: `7CEE 83C9 C621 B186 67DD 1BFE CAED 4975 DAB0 53A8`

## Manual Download

Packages are also available in [pool/main/](pool/main/).

## RPM Repository

Fedora/RHEL packages available at [yeager/rpm-repo](https://github.com/yeager/rpm-repo).

```bash
sudo tee /etc/yum.repos.d/yeager.repo << 'EOF'
[yeager]
name=Yeager's Translation Tools
baseurl=https://yeager.github.io/rpm-repo
enabled=1
gpgcheck=0
EOF
sudo dnf install l10n-lint po-translate
```

## Source Code

| Project | Repository |
|---------|------------|
| l10n-lint | [github.com/yeager/l10n-lint](https://github.com/yeager/l10n-lint) |
| po-translate | [github.com/yeager/po-translate](https://github.com/yeager/po-translate) |
| po-diff | [github.com/yeager/po-diff](https://github.com/yeager/po-diff) |
| tp-lint | [github.com/yeager/tp-lint](https://github.com/yeager/tp-lint) |
| traduco | [github.com/yeager/traduco](https://github.com/yeager/traduco) |

## License

All packages are GPL-3.0-or-later.

---
*Last updated: 2026-02-07*
