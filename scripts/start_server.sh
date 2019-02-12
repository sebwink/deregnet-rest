#!/bin/bash

declare -a allvars=(\
  "SERVER_ROOT" \
  "MONGO_HOST" \
  "MONGO_PORT" \
  "REDIS_HOST" \
  "REDIS_PORT" \
  "PYTHON_INTERP" \
  "HOST" \
  "PORT" \
  "SERVER_BACKEND" \
  "START_RUNNERS" \
  "NUM_RUNNERS" \
  "DEBUG"\
)

# defaults
# path of the server module root
SERVER_ROOT="$( cd "$(dirname "$0")" ; pwd -P )"/../server
# mongo host
MONGO_HOST=localhost
# mongo port
MONGO_PORT=27017
# redis host
REDIS_HOST=localhost
# redis port
REDIS_PORT=6379
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
NUM_RUNNERS=2
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
	    --mongo-host)
			START_MONGOD=false
			MONGO_HOST="$2"
			shift
			shift
			;;
		--mongo-port)
			START_MONGOD=false
			MONGO_PORT="$2"
			shift
			shift
			;;
		--redis-host)
			START_REDIS=false
			REDIS_HOST="$2"
			shift
			shift
			;;
		--redis-port)
			START_REDIS=false
			REDIS_PORT="$2"
			shift
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
			# global config file overwriting *anything*
			# set here (if variable is also in config file)
			DEREGNET_CONFIG_FILE="$2"
			shift
			shift
			;;
		--gunicorn)
			DEPLOY=gunicorn
			shift
			;;
		*)
            POSITIONAL+=("$1")
            shift
            ;;
	esac
done

set -- "${POSITIONAL[@]}"

# overwrite above defaults if config file is specified via DEREGNET_CONFIG_FILE:
if [ ! -z "$DEREGNET_CONFIG_FILE" ]; then
	for VAR in "${allvars[@]}"; do
		VALUE=$(cat $DEREGNET_CONFIG_FILE | shyaml get-value $VAR '')
		if [ ! -z "$VALUE" ]; then
			declare $VAR=$VALUE
		fi
	done
fi

# MongoDB
export MONGO_HOST
export MONGO_PORT
# Redis
export REDIS_HOST
export REDIS_PORT
# DeRegNet Server
export HOST
export PORT
export SERVER_BACKEND
export START_RUNNERS 
export NUM_RUNNERS
export DEBUG

cd $SERVER_ROOT/..

if [ -z "$DEPLOY" ]; then
  $PYTHON_INTERP -m server
else
  if [ $DEPLOY == 'gunicorn' ]; then
    gunicorn --config config/wsgi/gunicorn.py deregnet_rest:app
  fi
fi
