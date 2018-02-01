#!/bin/bash

# path of the server module root
SERVER_ROOT=server
# whether to start mongod
START_MONGOD=true
# mongod executable
MONGOD=mongod
# whether to start redis
START_REDIS=true
# redis-server executable
REDIS=redis-server
# python interpreter
PYTHON_INTERP=python3
# host on which to run the server
HOST=localhost
# port on which to run the server
PORT=8080
# server backend: flask, tornado or gevent
SERVER_BACKEND=flask
# whether to start the runner processes
START_RUNNERS=true
# whether to start the server in debug mode
DEBUG=false


# argument parsing from: https://stackoverflow.com/questions/192249

POSITIONAL=()
while [[ $# -gt 0 ]]; do
    key="$1"
	case $key in
		-s|--server-root)
			SERVER_ROOT="$2"
			shift
			shift
			;;
	    -m|--mongod-config)
			MONGOD_CONFIG="$2"
			shift
			shift
			;;
		--mongod-running)
			START_MONGOD=false
			shift
			;;
		-r|--redis-config)
			REDIS_CONFIG="$2"
			shift
			shift
			;;
		--redis-running)
			START_REDIS=false
			shift
			;;
		-i|--python-interp)
			PYTHON_INTERP="$2"
			shift
			shift
			;;
		-b|--server-backend)
			SERVER_BACKEND="$2"
			shift
			shift
			;;
		-h|--host)
			HOST="$2"
			shift
			shift
			;;
		-p|--port)
			PORT="$2"
			shift
			shift
			;;
		--no-runners)
			START_RUNNERS=false
			shift
			;;
		-d|--debug)
			DEBUG=true
			shift
			;;
		-c|--config-file)
			# global config file overwriting almost *anything* set here (if also in file)
			DEREGNET_REST_CONFIG="$2"
			export DEREGNET_REST_CONFIG
			shift
			shift
			;;
		*)
		    POSITIONAL+=("$1")
			shift
			;;
	esac
done
set -- "${POSITIONAL[@]}"

if [ -z "$MONGOD_CONFIG" ]; then
	MONGOD_CONFIG=$SERVER_ROOT/config/mongod.conf
fi

if [ -z "$REDIS_CONFIG" ]; then
	REDIS_CONFIG=$SERVER_ROOT/config/redis.conf
fi


# MongoDB
export MONGOD_CONFIG
export START_MONGOD
export MONGOD
# Redis
export REDIS_CONFIG
export START_REDIS
export REDIS
# Server
export HOST
export PORT
export SERVER_BACKEND
export START_RUNNERS
export DEBUG

$PYTHON_INTERP -m deregnet_rest
