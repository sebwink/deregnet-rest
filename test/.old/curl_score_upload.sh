#!/usr/bin/env bash

API_ROOT=${DEREGNET_API_ROOT:-https://dereg.net/deregnet}

CREDENTIALS="$@"

../curl -X POST \
     -H "Content-type: application/json" \
     -H "Authorization: Bearer $CREDENTIALS" \
     --data @score_data.json \
     --url $API_ROOT/score > score.json

cat score.json
