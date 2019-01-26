#!/usr/bin/env bash

API_ROOT=http://localhost:8000/deregnet

CREDENTIALS=$(echo "$@" | base64)

curl -X GET \
     -H "Authorization: Basic $CREDENTIALS" \
     --url $API_ROOT/runs
