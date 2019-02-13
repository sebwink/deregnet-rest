#!/usr/bin/env bash

DEREGNET_API_ROOT=https://dereg.net/deregnet

CREDENTIALS="$@"

# Initializing the graph

./generate_test_run.py

../curl -X POST \
     --url $DEREGNET_API_ROOT/run \
     -H "Authorization: Bearer $CREDENTIALS" \
     -H 'Content-Type: application/json' \
     --data @test_run.json > run_info.json

cat run_info.json
