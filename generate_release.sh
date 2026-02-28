#!/bin/bash
cd dists/stable

do_hash() {
    HASH_NAME=$1
    HASH_CMD=$2
    echo "${HASH_NAME}:"
    for f in $(find . -type f ! -name "Release*" ! -name "InRelease" | sort); do
        f=$(echo $f | cut -c3-)
        SIZE=$(wc -c < "$f" | tr -d ' ')
        HASH=$($HASH_CMD "$f" | cut -d' ' -f1)
        echo " ${HASH} ${SIZE} ${f}"
    done
}

cat << RELEASE
Origin: Danne L10n Suite
Label: Danne L10n Suite
Suite: stable
Codename: stable
Architectures: all amd64 arm64 armhf i386
Components: main
Description: Danne L10n Suite APT Repository
Date: $(LC_ALL=C date -u +"%a, %d %b %Y %H:%M:%S UTC")
$(do_hash "MD5Sum" "openssl md5 -r")
$(do_hash "SHA256" "openssl dgst -sha256 -r")
RELEASE
