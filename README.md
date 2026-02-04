# Debian Repository for Translation Tools

APT repository for **l10n-lint**, **tp-lint**, and **po-translate**.

## Quick Install

```bash
# Add repository
echo "deb [trusted=yes] https://yeager.github.io/debian-repo stable main" | sudo tee /etc/apt/sources.list.d/yeager.list

# Update and install
sudo apt update
sudo apt install l10n-lint tp-lint po-translate
```

## Available Packages

| Package | Version | Description |
|---------|---------|-------------|
| **l10n-lint** | 1.3.4 | Linter for localization files (.po, .ts) |
| **tp-lint** | 1.5.4 | Translation Project linter and statistics |
| **po-translate** | 1.3.3 | Batch translate PO and TS files |

## Manual Download

Packages are also available in [pool/main/](pool/main/).

## Source Code

- [l10n-lint](https://github.com/yeager/l10n-lint)
- [tp-lint](https://github.com/yeager/tp-lint)
- [po-translate](https://github.com/yeager/po-translate)

## License

All packages are GPL-3.0-or-later.
