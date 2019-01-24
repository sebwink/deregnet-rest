#!/usr/sh

set -e

curl -X POST \
     --url http://kong:8001/services \
     --data 'name=deregnet' \
     --data 'url=http://deregnet-rest:8080/deregnet/' > /dev/null

curl -X POST \
     --url http://kong:8001/services/deregnet/routes \
     --data 'hosts[]=dereg.net' \
     --data 'paths[]=/deregnet'
