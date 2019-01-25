#!/usr/bin/env bash

DEREGNET_API_ROOT=http://localhost:8000/deregnet

# Initializing the graph

./generate_test_run.py

#-H 'Magic-Token: 00000000-0000-0000-0000-000000000000' \
curl -X POST \
     --url $DEREGNET_API_ROOT/run \
     -H 'Content-Type: application/json' \
     --data @test_run.json > run_info.json

cat run_info.json
