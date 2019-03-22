#!/usr/bin/env bash

SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )" 
SECRETS=$SCRIPT_PATH/../.secrets

mkdir -p $SECRETS

openssl req -x509 -newkey rsa:4096 -keyout $SECRETS/ssl.key -out $SECRETS/ssl.crt -days 365 -subj '/CN=dereg.net' -nodes
