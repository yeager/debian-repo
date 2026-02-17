# Yeager Debian Repository

APT repository for Daniel Nylander's localization, development, and system tools.

## Quick Setup

```bash
curl -fsSL https://yeager.github.io/debian-repo/yeager-archive-keyring.gpg | sudo tee /usr/share/keyrings/yeager-archive-keyring.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/yeager-archive-keyring.gpg] https://yeager.github.io/debian-repo stable main" | sudo tee /etc/apt/sources.list.d/yeager.list
sudo apt update
```

## Available Packages (28)

### GUI Applications — Localization (GTK4/Adwaita)

| Package | Version | Description |
|---------|---------|-------------|
| [cldr-viewer](https://github.com/yeager/cldr-viewer) | 0.1.8 | Browse and compare Unicode CLDR locale data |
| [commonvoice-status](https://github.com/yeager/commonvoice-status) | 0.1.8 | Mozilla Common Voice recording statistics |
| [ddtp-translate](https://github.com/yeager/ddtp-translate) | 0.7.0 | Translate Debian package descriptions via DDTSS |
| [desktop-editor](https://github.com/yeager/desktop-editor) | 0.2.7 | Visual .desktop file editor with translation support |
| [elementary-l10n](https://github.com/yeager/elementary-l10n) | 0.3.1 | elementary OS translation status via Weblate |
| [font-preview](https://github.com/yeager/font-preview) | 0.2.8 | Preview and compare installed fonts |
| [github-l10n](https://github.com/yeager/github-l10n) | 0.2.6 | Scan GitHub repos for missing translations |
| [l10n-glossary](https://github.com/yeager/l10n-glossary) | 0.2.6 | Translation glossary editor (TBX/CSV/TSV) |
| [l10n-preview](https://github.com/yeager/l10n-preview) | 0.2.6 | Preview translations with quality indicators |
| [langpack-inspector](https://github.com/yeager/langpack-inspector) | 0.2.5 | Inspect Ubuntu language pack coverage |
| [libretranslate-gui](https://github.com/yeager/libretranslate-gui) | 0.2.6 | LibreTranslate desktop client |
| [locale-tester](https://github.com/yeager/locale-tester) | 0.2.6 | Test locale formatting (dates, numbers, currency) |
| [snap-l10n](https://github.com/yeager/snap-l10n) | 0.2.7 | Snap Store translation coverage dashboard |
| [tm-manager](https://github.com/yeager/tm-manager) | 0.2.8 | Translation memory manager (TMX/TBX) |
| [ubuntu-l10n](https://github.com/yeager/ubuntu-l10n) | 0.3.4 | Ubuntu/Launchpad translation statistics |
| vsdview 0.1.2 | Read-only viewer for Microsoft Visio files |

### GUI Applications — System & Network (GTK4/Adwaita)

| Package | Version | Description |
|---------|---------|-------------|
| [bildstod](https://github.com/yeager/bildstod) | 0.1.0 | Visual schedule and picture support tool (for users with autism/language disorders) |
| [cve-monitor](https://github.com/yeager/cve-monitor) | 0.1.0 | Monitor CVE vulnerabilities for installed packages |
| [ha-l10n](https://github.com/yeager/ha-l10n) | 0.1.0 | Home Assistant translation status dashboard |
| [mqtt-inspector](https://github.com/yeager/mqtt-inspector) | 0.1.0 | MQTT message inspector for IoT debugging |
| [obd2-viewer](https://github.com/yeager/obd2-viewer) | 0.1.0 | OBD2 diagnostic data viewer and logger |
| [packetlens](https://github.com/yeager/pcap-viewer) | 0.2.5 | Network packet analyzer (pcap/pcapng) |
| [tts-tester](https://github.com/yeager/tts-tester) | 0.1.0 | Text-to-speech engine comparison tool |

### CLI Tools

| Package | Version | Description |
|---------|---------|-------------|
| [l10n-conv](https://github.com/yeager/l10n-conv) | 1.0.4 | Convert between translation formats (PO↔XLIFF↔TS↔JSON) |
| [l10n-lint](https://github.com/yeager/l10n-lint) | 1.15.8 | Linter for .po and .ts translation files (CLI + GTK GUI) |
| [po-diff](https://github.com/yeager/po-diff) | 1.0.0 | Compare PO/XLIFF files and show translation differences |
| [po-translate](https://github.com/yeager/po-translate) | 1.5.4 | Machine-translate PO files via multiple backends |
| [svlang](https://github.com/yeager/svlang) | 0.1.5 | Swedish language quality checker for translations |
| [tp-lint](https://github.com/yeager/tp-lint) | 1.8.3 | Translation Project metadata validator |

## GPG Key

The repository is signed with key `DAB053A8`. Import it:

```bash
curl -fsSL https://yeager.github.io/debian-repo/yeager-archive-keyring.gpg | sudo tee /usr/share/keyrings/yeager-archive-keyring.gpg > /dev/null
```

## RPM Repository

Fedora/RHEL packages are available at [yeager/rpm-repo](https://github.com/yeager/rpm-repo).

## Source Code

All packages are open source (GPL-3.0) and hosted at [github.com/yeager](https://github.com/yeager/).

## Translations

Help translate these apps on [Transifex](https://app.transifex.com/danielnylander/).
