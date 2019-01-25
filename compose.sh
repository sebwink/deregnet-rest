#!/usr/bin/env bash

export KONG_PG_DATABASE=kongdb
export KONG_PG_USER=kongdb
export KONG_PG_PASSWORD=dev

docker-compose $@
