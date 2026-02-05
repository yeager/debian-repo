# Yeager's Debian Repository

APT repository for **l10n-lint**, **tp-lint**, **po-translate**, and **po-diff**.

## Quick Install

```bash
# Add GPG key
curl -fsSL https://yeager.github.io/debian-repo/yeager.gpg | sudo gpg --dearmor -o /usr/share/keyrings/yeager.gpg

# Add repository
echo 'deb [signed-by=/usr/share/keyrings/yeager.gpg] https://yeager.github.io/debian-repo stable main' | sudo tee /etc/apt/sources.list.d/yeager.list

# Update and install
sudo apt update
sudo apt install l10n-lint tp-lint po-translate
```

## Available Packages

| Package | Version | Description |
|---------|---------|-------------|
| **l10n-lint** | 1.10.0 | Linter for localization files (.po, .ts) |
| **tp-lint** | 1.8.0 | Translation Project linter and statistics |
| **po-translate** | 1.4.0 | Batch translate PO and TS files |
| **po-diff** | 1.0.0 | Compare and diff PO files |

## GPG Signing

Repository is signed with GPG key `CAED4975DAB053A8`.

- Public key: [yeager.gpg](yeager.gpg)
- Fingerprint: `7CEE 83C9 C621 B186 67DD 1BFE CAED 4975 DAB0 53A8`

## Manual Download

Packages are also available in [pool/main/](pool/main/).

## RPM Packages

RPM packages are available on GitHub Releases:
- [l10n-lint releases](https://github.com/yeager/l10n-lint/releases)
- [tp-lint releases](https://github.com/yeager/tp-lint/releases)
- [po-translate releases](https://github.com/yeager/po-translate/releases)

## Source Code

- [l10n-lint](https://github.com/yeager/l10n-lint) - Localization file linter
- [tp-lint](https://github.com/yeager/tp-lint) - Translation Project statistics
- [po-translate](https://github.com/yeager/po-translate) - Batch translation tool
- [po-diff](https://github.com/yeager/po-diff) - PO file comparison

## License

All packages are GPL-3.0-or-later.
