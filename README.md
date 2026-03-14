# Nylander L10n Suite - Debian Repository

Daniel Nylander's localization and development packages.

## Installation

### Method 1: Modern apt (Recommended)

```bash
# Download and install GPG key
wget -qO /tmp/yeager-repo-key.asc https://yeager.github.io/debian-repo/yeager-repo-key.asc
sudo cp /tmp/yeager-repo-key.asc /usr/share/keyrings/yeager-repo.asc

# Add repository
echo 'deb [signed-by=/usr/share/keyrings/yeager-repo.asc] https://yeager.github.io/debian-repo/ stable main' | sudo tee /etc/apt/sources.list.d/yeager.list

# Update and install
sudo apt update
sudo apt install <package-name>
```

### Method 2: Legacy apt-key (Deprecated)

```bash
# Add GPG key (legacy method)
wget -qO - https://yeager.github.io/debian-repo/yeager-repo-key.asc | sudo apt-key add -

# Add repository  
echo 'deb https://yeager.github.io/debian-repo/ stable main' | sudo tee /etc/apt/sources.list.d/yeager.list

# Update and install
sudo apt update
sudo apt install <package-name>
```

## GPG Key Information

- **Key ID**: DAB053A8
- **Fingerprint**: 7CEE 83C9 C621 B186 67DD 1BFE CAED 4975 DAB0 53A8
- **Owner**: Yeager Debian Repository <daniel@danielnylander.se>

## Available Packages

This repository contains Swedish localization tools and applications including:

- libspiel: Speech synthesis library
- l10n-lint: Translation file linting tool
- Various GTK4/Adwaita applications for autism support
- Development tools for localization

## Support

For issues and questions: daniel@danielnylander.se