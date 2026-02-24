# Danne L10n Suite - Debian Repository

Debian package repository for the Danne L10n Suite applications.

**Packages:** 71

## Setup

### Add GPG key
```bash
curl -fsSL https://yeager.github.io/debian-repo/yeager.gpg | sudo gpg --dearmor -o /usr/share/keyrings/yeager.gpg
```

### Add repository
```bash
echo "deb [signed-by=/usr/share/keyrings/yeager.gpg] https://yeager.github.io/debian-repo stable main" | sudo tee /etc/apt/sources.list.d/yeager.list
```

### Update and install
```bash
sudo apt update
sudo apt install <package-name>
```

## Available Packages

| Package | Version |
|---------|---------|
| anpr-viewer | 0.4.0 |
| apt-changelog-viewer | 0.1.3 |
| autopkgtest-runner | 0.1.3 |
| beloningskartan | 0.1.7 |
| bildordbok | 0.3.6 |
| bildschema | 0.3.5 |
| bildstod | 0.4.7 |
| build-log-analyzer | 0.1.3 |
| cert-watch | 0.1.4 |
| cldr-viewer | 0.1.9 |
| commonvoice-status | 0.1.9 |
| cve-monitor | 0.3.5 |
| ddtp-translate | 0.14.2 |
| debian-installer-companion | 0.1.3 |
| debian-policy-checker | 0.1.3 |
| dep-graph-viewer | 0.1.3 |
| desktop-editor | 0.2.9 |
| elementary-l10n | 0.4.0 |
| firewall-manager | 0.1.4 |
| fokuskompis | 0.2.4 |
| font-preview | 0.2.9 |
| gettext-coverage | 0.1.3 |
| github-l10n | 0.2.7 |
| gnome-l10n | 0.2.4 |
| ha-l10n | 0.2.4 |
| kanslokartan | 0.1.7 |
| l10n-conv | 1.0.9-1 |
| l10n-glossary | 0.2.10 |
| l10n-lint | 1.16.0 |
| l10n-preview | 0.2.7 |
| langpack-inspector | 0.2.9 |
| libretranslate-gui | 0.2.7 |
| ljudladan | 0.1.6 |
| locale-tester | 0.2.7 |
| log-viewer | 0.1.4 |
| lp-bug-triager | 0.1.3 |
| lugnarummet | 0.3.2 |
| makebread | 0.4.3 |
| mentor-dashboard | 0.1.3 |
| merge-o-matic-viewer | 0.1.3 |
| minnet | 0.1.7 |
| mittschema | 0.1.5 |
| mqtt-dashboard | 0.1.4 |
| mqtt-inspector | 0.2.4 |
| new-queue-monitor | 0.1.3 |
| obd2-viewer | 0.2.4 |
| ordbyggaren | 0.2.5 |
| packetlens | 0.2.7 |
| pecsbrada | 0.3.5 |
| po-diff | 1.0.1 |
| po-review-board | 0.1.3 |
| po-translate | 1.5.7 |
| process-explorer | 0.1.4 |
| regex-tester | 0.1.4 |
| release-notes-editor | 0.1.3 |
| rutinkompis | 0.3.5 |
| scummvm-gtk | 0.2.3 |
| snap-l10n | 0.2.12 |
| socialaberattelser | 0.1.7 |
| svlang | 0.1.7-1 |
| sysinfo-gtk | 0.1.2 |
| tidskollen | 0.2.5 |
| tm-manager | 0.2.12 |
| tp-lint | 1.8.4-1 |
| tp-status | 0.2.0 |
| transition-tracker | 0.1.1 |
| tts-tester | 0.2.4 |
| ubuntu-l10n | 0.3.6 |
| vsdview | 0.4.6 |
| wifi-analyzer | 0.1.4 |
| zigbee-manager | 0.1.4 |

## License

See individual packages for their respective licenses.
