#!/bin/bash
cd dists/stable

# Generate checksums
do_hash() {
    HASH_NAME=$1
    HASH_CMD=$2
    echo "${HASH_NAME}:"
    for f in $(find . -type f ! -name "Release*" ! -name "InRelease"); do
        f=$(echo $f | cut -c3-)
        SIZE=$(wc -c < "$f" | tr -d ' ')
        HASH=$($HASH_CMD "$f" | cut -d' ' -f1)
        echo " ${HASH} ${SIZE} ${f}"
    done
}

cat << RELEASE
Origin: Yeager
Label: Yeager's Translation Tools
Suite: stable
Codename: stable
Version: 1.0
Architectures: amd64 arm64
Components: main
Description: Yeager's Translation Tools APT Repository
Date: $(date -Ru)
$(do_hash "SHA256" "openssl dgst -sha256 -r")
RELEASE
