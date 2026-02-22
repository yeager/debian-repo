# Yeager Debian Repository

APT repository with translation tools, accessibility apps, and system utilities by Daniel Nylander.

## Installation

```bash
# Add GPG key
curl -fsSL https://yeager.github.io/debian-repo/yeager.gpg | sudo gpg --dearmor -o /usr/share/keyrings/yeager.gpg

# Add repository
echo "deb [signed-by=/usr/share/keyrings/yeager.gpg] https://yeager.github.io/debian-repo stable main" | sudo tee /etc/apt/sources.list.d/yeager.list

# Update and install
sudo apt update
```

## Packages

72 packages across these categories:

### Accessibility / Children (15 apps)
Apps for children with autism, ADHD, and language disorders.

| Package | Description |
|---------|-------------|
| beloningskartan | Visual reward system with stars and goals |
| bildordbok | Picture dictionary with ARASAAC pictograms |
| bildschema | Visual daily schedule with ARASAAC |
| bildstod | Visual communication with ARASAAC |
| fokuskompis | Focus and task manager for ADHD/autism |
| kanslokartan | Emotion recognition and journal |
| ljudladan | Sound sensitivity tool |
| lugnarummet | Sensory regulation and calming strategies |
| minnet | Working memory training games |
| mittschema | Weekly visual schedule |
| ordbyggaren | Phonological training |
| pecsbrada | Digital PECS communication board |
| rutinkompis | Step-by-step visual routine guides |
| socialaberattelser | Social stories with images |
| tidskollen | Visual time timer |

### Translation & Localization (27 tools)
| Package | Description |
|---------|-------------|
| cldr-viewer | Unicode CLDR locale data viewer |
| commonvoice-status | Mozilla Common Voice statistics |
| ddtp-translate | Debian description translation tool |
| desktop-editor | .desktop file editor |
| elementary-l10n | elementary OS translation status |
| fedora-l10n | Fedora Weblate translation status |
| font-preview | Font browser with Unicode coverage |
| gettext-coverage | Translation coverage per package |
| github-l10n | GitHub repo translation scanner |
| gnome-l10n | GNOME translation statistics |
| ha-l10n | Home Assistant translation status |
| l10n-conv | Localization file converter (CLI) |
| l10n-glossary | Terminology editor |
| l10n-lint | Localization file linter (CLI) |
| l10n-preview | Translation preview in simulated UI |
| langpack-inspector | Ubuntu language pack inspector |
| libretranslate-gui | LibreTranslate frontend |
| linguaedit | Translation file editor (Qt6) |
| locale-tester | Locale behavior tester |
| po-diff | PO/TS file diff tool (CLI) |
| po-review-board | PO review with diff and approval |
| po-translate | Batch AI translation for PO/TS (CLI) |
| snap-l10n | Snap package translation status |
| svlang | Swedish NLP toolkit (CLI) |
| tm-manager | Translation Memory (TMX) manager |
| tp-lint | Translation Project linter (CLI) |
| tp-status | Translation Project status viewer |
| ubuntu-l10n | Ubuntu/Launchpad translation statistics |

### Debian/Ubuntu Development (14 tools)
| Package | Description |
|---------|-------------|
| apt-changelog-viewer | Package changelog viewer |
| autopkgtest-runner | Autopkgtest frontend |
| build-log-analyzer | Build log analyzer |
| debian-installer-companion | Installation companion |
| debian-policy-checker | Policy validator |
| dep-graph-viewer | Dependency graph viewer |
| lp-bug-triager | Launchpad bug triage |
| mentor-dashboard | Debian Mentors dashboard |
| merge-o-matic-viewer | Ubuntu-Debian sync helper |
| new-queue-monitor | FTP NEW queue monitor |
| po-review-board | PO translation review |
| release-notes-editor | Release notes editor |
| transition-tracker | Library transition tracker |
| gettext-coverage | Translation coverage viewer |

### System & Network (10 tools)
| Package | Description |
|---------|-------------|
| anpr-viewer | License plate recognition from video |
| cert-watch | TLS certificate expiry monitor |
| cve-monitor | CVE vulnerability monitor |
| firewall-manager | UFW/nftables firewall manager |
| log-viewer | Structured log viewer |
| mqtt-dashboard | MQTT IoT dashboard |
| mqtt-inspector | MQTT message inspector |
| obd2-viewer | OBD2 diagnostic viewer |
| packetlens | PCAP network analyzer |
| process-explorer | Process explorer |
| regex-tester | Regular expression tester |
| scummvm-gtk | ScummVM game launcher |
| sysinfo-gtk | System information viewer |
| wifi-analyzer | Wi-Fi signal analyzer |
| zigbee-manager | Zigbee device manager |

### Other
| Package | Description |
|---------|-------------|
| kodi-subtitle-translator | Kodi subtitle auto-translator |
| makebread | Bread machine recipe manager |
| vsdview | Microsoft Visio file viewer |

## Author

Daniel Nylander — [danielnylander.se](https://danielnylander.se)
