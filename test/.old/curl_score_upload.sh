#!/usr/bin/env bash

API_ROOT=http://localhost:8000/deregnet

CREDENTIALS=$(echo "$@" | base64)

curl -X POST \
     -H "Content-type: application/json" \
     -H "Authorization: Basic $CREDENTIALS" \
     --data @score_data.json \
     --url $API_ROOT/score > score.json

cat score.json
