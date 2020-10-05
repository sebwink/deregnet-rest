#!/usr/bin/env bash

API_ROOT=https://dereg.net/deregnet

CREDENTIALS="$@"

../curl -X GET \
     -H "Authorization: Bearer $CREDENTIALS" \
     --url $API_ROOT/scores
