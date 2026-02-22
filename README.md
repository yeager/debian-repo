# Yeager Debian Repository

APT-repo med översättningsverktyg, tillgänglighetsappar och systemverktyg av Daniel Nylander.

## Installation

### DEB822 (Ubuntu 24.04+ / Debian 12+)

```bash
curl -fsSL https://yeager.github.io/debian-repo/yeager-archive-keyring.gpg | sudo tee /usr/share/keyrings/yeager-archive-keyring.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/yeager.sources << 'EOF'
Types: deb
URIs: https://yeager.github.io/debian-repo
Suites: stable
Components: main
Signed-By: /usr/share/keyrings/yeager-archive-keyring.gpg
EOF
sudo apt update
```

### Enradsformat

```bash
curl -fsSL https://yeager.github.io/debian-repo/yeager-archive-keyring.gpg | sudo tee /usr/share/keyrings/yeager-archive-keyring.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/yeager-archive-keyring.gpg] https://yeager.github.io/debian-repo stable main" | sudo tee /etc/apt/sources.list.d/yeager.list
sudo apt update
```

## Paket (37 st)

### Översättning/L10n — GUI (GTK4/Adwaita)

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| [cldr-viewer](https://github.com/yeager/cldr-viewer) | 0.1.9 | Unicode CLDR-data, jämför locale |
| [commonvoice-status](https://github.com/yeager/commonvoice-status) | 0.1.9 | Mozilla Common Voice statistik |
| [ddtp-translate](https://github.com/yeager/ddtp-translate) | 0.13.0 | Översätt Debian-paketbeskrivningar via DDTSS |
| [desktop-editor](https://github.com/yeager/desktop-editor) | 0.2.8 | .desktop-filredigerare med översättningsstöd |
| [elementary-l10n](https://github.com/yeager/elementary-l10n) | 0.3.2 | elementary OS översättningsstatus |
| [font-preview](https://github.com/yeager/font-preview) | 0.2.9 | Förhandsgranska och jämför typsnitt |
| [github-l10n](https://github.com/yeager/github-l10n) | 0.2.7 | Hitta saknade översättningar i GitHub-repon |
| [gnome-l10n](https://github.com/yeager/gnome-l10n) | 0.2.1 | GNOME översättningsstatistik |
| [l10n-glossary](https://github.com/yeager/l10n-glossary) | 0.2.7 | Terminologiredigerare (TBX/CSV/TSV) |
| [l10n-preview](https://github.com/yeager/l10n-preview) | 0.2.7 | Förhandsgranska översättningar med kvalitetsindikatorer |
| [langpack-inspector](https://github.com/yeager/langpack-inspector) | 0.2.6 | Inspektera Ubuntu-språkpaket |
| [libretranslate-gui](https://github.com/yeager/libretranslate-gui) | 0.2.7 | LibreTranslate skrivbordsklient |
| [linguaedit](https://github.com/yeager/linguaedit) | 1.8.14 | PO-filredigerare (PySide6) |
| [locale-tester](https://github.com/yeager/locale-tester) | 0.2.7 | Testa locale-formatering (datum, tal, valuta) |
| [po-review-board](https://github.com/yeager/po-review-board) | 0.1.0 | Granska .po-översättningar med diff och godkännande |
| [snap-l10n](https://github.com/yeager/snap-l10n) | 0.2.9 | Snap Store översättningsstatus |
| [tm-manager](https://github.com/yeager/tm-manager) | 0.2.9 | Översättningsminne (TMX/TBX) |
| [ubuntu-l10n](https://github.com/yeager/ubuntu-l10n) | 0.3.5 | Ubuntu/Launchpad översättningsstatistik |
| [vsdview](https://github.com/yeager/vsdview) | 0.4.2 | Microsoft Visio-filvisare |
| [gettext-coverage](https://github.com/yeager/gettext-coverage) | 0.1.0 | Översättningsgrad per paket i en distro |

### Översättning/L10n — CLI

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| [l10n-conv](https://github.com/yeager/l10n-conv) | 1.0.9 | Konvertera mellan PO/XLIFF/TS/JSON |
| [l10n-lint](https://github.com/yeager/l10n-lint) | 1.16.0 | Linter för översättningsfiler |
| [po-diff](https://github.com/yeager/po-diff) | 1.0.1 | Jämför PO/TS-filer |
| [po-translate](https://github.com/yeager/po-translate) | 1.5.7 | Batch-översätt PO/TS med AI |
| [svlang](https://github.com/yeager/svlang) | 0.1.7 | Kontrollera svensk språkkvalitet |
| [tp-lint](https://github.com/yeager/tp-lint) | 1.8.4 | Linter för översättningsprojekt |

### Barn/Tillgänglighet (GTK4/Adwaita)

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| [bildordbok](https://github.com/yeager/bildordbok) | 0.3.2 | Bildordbok med ARASAAC-stöd |
| [bildschema](https://github.com/yeager/bildschema) | 0.3.2 | Visuella scheman med ARASAAC |
| [bildstod](https://github.com/yeager/bildstod) | 0.4.4 | Bildstöd med ARASAAC-piktogram |
| [beloningskartan](https://github.com/yeager/beloningskartan) | 0.1.2 | Belöningskarta |
| [fokuskompis](https://github.com/yeager/fokuskompis) | 0.2.2 | Fokushjälp med timer |
| [kanslokartan](https://github.com/yeager/kanslokartan) | 0.1.2 | Känslokartan — identifiera känslor |
| [ljudladan](https://github.com/yeager/ljudladan) | 0.1.2 | Ljudbibliotek för avslappning |
| [lugnarummet](https://github.com/yeager/lugnarummet) | 0.3.1 | Lugnt rum — avslappning och sinnesro |
| [minnet](https://github.com/yeager/minnet) | 0.1.2 | Minnesträningsspel |
| [mittschema](https://github.com/yeager/mittschema) | 0.1.2 | Dagschema med bilder |
| [ordbyggaren](https://github.com/yeager/ordbyggaren) | 0.2.1 | Ordbyggare — träna stavning |
| [pecsbrada](https://github.com/yeager/pecsbrada) | 0.3.2 | PECS-kommunikationsbräda |
| [rutinkompis](https://github.com/yeager/rutinkompis) | 0.3.2 | Rutinkompis med ARASAAC |
| [socialaberattelser](https://github.com/yeager/socialaberattelser) | 0.1.2 | Sociala berättelser |
| [tidskollen](https://github.com/yeager/tidskollen) | 0.2.1 | Visuell tidskoll |

### Nätverk/Säkerhet/System (GTK4/Adwaita)

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| [anpr-viewer](https://github.com/yeager/anpr-viewer) | 0.3.0 | Registreringsskyltsigenkänning (video + kamera) |
| [cert-watch](https://github.com/yeager/cert-watch) | 0.1.1 | TLS-certifikatövervakning |
| [cve-monitor](https://github.com/yeager/cve-monitor) | 0.3.5 | CVE-sårbarhetsbevakning |
| [firewall-manager](https://github.com/yeager/firewall-manager) | 0.1.1 | ufw/nftables-gränssnitt |
| [ha-l10n](https://github.com/yeager/ha-l10n) | 0.2.1 | Home Assistant översättningsstatus |
| [log-viewer](https://github.com/yeager/log-viewer) | 0.1.1 | Journalctl-loggvisare |
| [mqtt-dashboard](https://github.com/yeager/mqtt-dashboard) | 0.1.1 | MQTT-dashboard |
| [mqtt-inspector](https://github.com/yeager/mqtt-inspector) | 0.2.1 | MQTT-meddelandeinspektör |
| [obd2-viewer](https://github.com/yeager/obd2-viewer) | 0.2.1 | OBD2-diagnostikvisare |
| [packetlens](https://github.com/yeager/pcap-viewer) | 0.2.6 | Nätverkspaketanalys |
| [process-explorer](https://github.com/yeager/process-explorer) | 0.1.1 | Processhanterare |
| [regex-tester](https://github.com/yeager/regex-tester) | 0.1.1 | Visuell regex-testare |
| [tts-tester](https://github.com/yeager/tts-tester) | 0.2.1 | Text-till-tal-jämförelse |
| [wifi-analyzer](https://github.com/yeager/wifi-analyzer) | 0.1.1 | WiFi-kanalanalys |
| [zigbee-manager](https://github.com/yeager/zigbee-manager) | 0.1.1 | Zigbee-enhetshanterare |

### Övrigt — GUI (GTK4/Adwaita)

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| [makebread](https://github.com/yeager/makebread) | 0.4.0 | Recepthanterare för brödbak |
| [scummvm-gtk](https://github.com/yeager/scummvm-gtk) | 0.1.0 | GTK4-gränssnitt för ScummVM |

### Debian/Ubuntu-utveckling (GTK4/Adwaita) — .deb only

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| [apt-changelog-viewer](https://github.com/yeager/apt-changelog-viewer) | 0.1.0 | Visa changelogs med säkerhetsmarkeringar |
| [autopkgtest-runner](https://github.com/yeager/autopkgtest-runner) | 0.1.0 | Kör autopkgtest lokalt |
| [build-log-analyzer](https://github.com/yeager/build-log-analyzer) | 0.1.0 | Analysera sbuild/pbuilder-loggar |
| [debian-installer-companion](https://github.com/yeager/debian-installer-companion) | 0.1.0 | Installationsguide med hårdvarukontroll |
| [debian-policy-checker](https://github.com/yeager/debian-policy-checker) | 0.1.0 | Validera mot Debian Policy Manual |
| [dep-graph-viewer](https://github.com/yeager/dep-graph-viewer) | 0.1.0 | Visualisera paketberoenden |
| [lp-bug-triager](https://github.com/yeager/lp-bug-triager) | 0.1.0 | Launchpad-buggsortering |
| [mentor-dashboard](https://github.com/yeager/mentor-dashboard) | 0.1.0 | Debian Mentors-dashboard |
| [merge-o-matic-viewer](https://github.com/yeager/merge-o-matic-viewer) | 0.1.0 | Ubuntu-Debian merge-hjälp |
| [new-queue-monitor](https://github.com/yeager/new-queue-monitor) | 0.1.0 | Bevaka Debian FTP NEW-kön |
| [release-notes-editor](https://github.com/yeager/release-notes-editor) | 0.1.0 | Release notes med mallar |
| [transition-tracker](https://github.com/yeager/transition-tracker) | 0.1.0 | Spåra biblioteksövergångar |

## Nyckel

GPG-nyckel: `DAB053A8`

## Underhållare

Daniel Nylander <daniel@danielnylander.se>
