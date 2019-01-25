#!/usr/bin/env bash

API_ROOT=http://localhost:8000/deregnet

curl -X POST \
     -H "Content-type: application/json" \
     --data @score_data.json \
     --url $API_ROOT/score > score.json

cat score.json
