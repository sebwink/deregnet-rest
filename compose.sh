#!/usr/bin/env bash

export DEREGNET_PORT=8181

export KONG_PG_DATABASE=test
export KONG_PG_USER=test
export KONG_PG_PASSWORD=test123

docker-compose $@
