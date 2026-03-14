#!/bin/bash
cd dists/stable

do_hash() {
    HASH_NAME=$1
    HASH_CMD=$2
    echo "${HASH_NAME}:"
    for f in $(find . -type f ! -name "Release*" ! -name "InRelease" | sort); do
        f=$(echo $f | cut -c3-)
        SIZE=$(wc -c < "$f" | tr -d " ")
        HASH=$(${HASH_CMD} "$f" | cut -d" " -f1)
        echo " ${HASH} ${SIZE} ${f}"
    done
}

cat << RELEASE
Origin: Nylander L10n Suite
Label: Nylander L10n Suite
Suite: stable
Codename: stable
Architectures: amd64
Components: main
Description: Daniel Nylander's localization and development packages
Date: $(LC_ALL=C date -u +"%a, %d %b %Y %H:%M:%S +0000")
$(do_hash "MD5Sum" "openssl dgst -md5 -r")
$(do_hash "SHA1" "openssl dgst -sha1 -r")
$(do_hash "SHA256" "openssl dgst -sha256 -r")
RELEASE
