#!/usr/bin/env bash

DEREGNET_API_ROOT=http://localhost:8000/deregnet

CREDENTIALS=$(echo "$@" | base64)

curl -X GET \
	 -H "Authorization: Basic $CREDENTIALS" \
     --url $DEREGNET_API_ROOT/graphs
