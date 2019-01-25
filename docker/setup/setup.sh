#!/usr/sh

set -e

echo "Register deregnet service"
curl --silent -X POST \
     --url http://kong:8001/services \
     --data 'name=deregnet' \
     --data 'url=http://deregnet-rest:8080/deregnet/' > /dev/null

echo "Setting route and path of deregnet service"
curl --silent -X POST \
     --url http://kong:8001/services/deregnet/routes \
     --data 'paths[]=/deregnet' \
     --data 'methods[]=GET' \
     --data 'methods[]=POST' \
     --data 'methods[]=DELETE' > /dev/null
