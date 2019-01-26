#!/usr/bin/env bash

DEREGNET_API_ROOT=http://localhost:8000/deregnet

# Initializing the graph

CREDENTIALS=$(echo "$@" | base64)

#-H 'Magic-Token: 00000000-0000-0000-0000-000000000000' \
curl -X POST \
     --url $DEREGNET_API_ROOT/graph \
     -H 'Content-Type: application/json' \
     -H "Authorization: Basic $CREDENTIALS" \
     --data @initial_graph_info.json > graph_info.json

cat graph_info.json

# Getting graph id

graph_id=$(python3 get_graph_id.py graph_info.json)

# Uploading the graphml

curl -X POST \
     -F "file_to_upload=@kegg_hsa.graphml.gz" \
     -H "Authorization: Basic $CREDENTIALS" \
     --url $DEREGNET_API_ROOT/graph/$graph_id

curl -X GET \
     -H "Authorization: Basic $CREDENTIALS" \
     --url $DEREGNET_API_ROOT/graph/$graph_id
