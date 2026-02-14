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
```

## Available Packages

### Translation Status Dashboards
| Package | Version | Description |
|---------|---------|-------------|
| **ubuntu-l10n** | 0.1.0 | Ubuntu translation status via Launchpad API |
| **elementary-l10n** | 0.1.0 | elementary OS translation status via Weblate |
| **langpack-inspector** | 0.1.0 | Inspect Ubuntu language packs, find missing translations |
| **snap-l10n** | 0.1.0 | Snap package translation status |

### Translation Tools
| Package | Version | Description |
|---------|---------|-------------|
| **linguaedit** | 1.8.14 | Professional translation editor (PO, TS, XLIFF) |
| **tm-manager** | 0.1.0 | Translation Memory manager (TMX) with fuzzy search |
| **l10n-glossary** | 0.1.0 | Glossary/terminology editor with consistency checking |
| **l10n-preview** | 0.1.0 | Preview PO/TS translations in simulated UI elements |
| **desktop-editor** | 0.1.0 | Visual .desktop file editor with validation |

### Quality & Testing
| Package | Version | Description |
|---------|---------|-------------|
| **locale-tester** | 0.1.0 | Compare locale settings side by side |
| **l10n-lint** | 1.14.9 | Linter for localization files (.po, .ts) |
| **l10n-lint-gtk** | 1.2.9 | GTK4 graphical interface for l10n-lint |
| **l10n-conv** | 1.0.0 | Universal l10n file converter (16 formats) |
| **font-preview** | 0.1.0 | Font browser with Unicode coverage per language |

### Utilities
| Package | Version | Description |
|---------|---------|-------------|
| **po-translate** | 1.5.0 | Batch translate PO/XLIFF files with DeepL |
| **po-diff** | 1.0.0 | Compare and diff PO files |
| **tp-lint** | 1.8.0 | Translation Project linter and statistics |
| **makebread** | 0.3.0 | Bread machine recipe manager |

## GPG Signing

All packages are signed with GPG key `DAB053A8`.

## Author

Daniel Nylander — [daniel@danielnylander.se](mailto:daniel@danielnylander.se)
https://danielnylander.se
