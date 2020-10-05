#!/usr/bin/env bash

DEREGNET_API_ROOT=https://dereg.net/deregnet

CREDENTIALS="$@"

../curl -X GET \
     -H "Authorization: Bearer $CREDENTIALS" \
     --url $DEREGNET_API_ROOT/graphs
