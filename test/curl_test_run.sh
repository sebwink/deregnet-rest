#!/usr/bin/env bash

DEREGNET_API_ROOT=http://localhost:8000/deregnet

CREDENTIALS=$(echo "$@" | base64)

# Initializing the graph

./generate_test_run.py

curl -X POST \
     --url $DEREGNET_API_ROOT/run \
     -H "Authorization: Basic $CREDENTIALS" \
     -H 'Content-Type: application/json' \
     --data @test_run.json > run_info.json

cat run_info.json
