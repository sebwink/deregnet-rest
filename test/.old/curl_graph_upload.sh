#!/usr/bin/env bash

API_ROOT=${DEREGNET_API_ROOT:-https://dereg.net/deregnet}

# Initializing the graph

CREDENTIALS="$@"

../curl -X POST \
     --url $API_ROOT/graph \
     -H 'Content-Type: application/json' \
     -H "Authorization: Bearer $CREDENTIALS" \
     --data @initial_graph_info.json > graph_info.json

cat graph_info.json

# Getting graph id

graph_id=$(python3 get_graph_id.py graph_info.json)

# Uploading the graphml

../curl -X POST \
     -F "file_to_upload=@kegg_hsa.graphml.gz" \
     -H "Authorization: Bearer $CREDENTIALS" \
     --url $API_ROOT/graph/$graph_id

../curl -X GET \
     -H "Authorization: Bearer $CREDENTIALS" \
     --url $API_ROOT/graph/$graph_id
