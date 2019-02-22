#!/bin/bash

declare -a allvars=(\
  "SERVER_ROOT" \
  "MONGO_HOST" \
  "MONGO_PORT" \
  "REDIS_HOST" \
  "REDIS_PORT" \
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
		-c|--config-file)
			# global config file overwriting *anything*
			# set here (if variable is also in config file)
			DEREGNET_CONFIG_FILE="$2"
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

cd $SERVER_ROOT/..

celery -A server.tasks.find_subgraphs:celery worker -l info -Q runs -E
