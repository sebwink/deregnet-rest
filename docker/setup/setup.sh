#!/usr/sh

set -e

ENV="${ENV:-development}"

function add_consumer {
  username=$1
  password=$2
  curl --silent -X POST \
       --url http://kong:8001/consumers \
       --data "username=$username" > /dev/null
  curl --silent -X POST \
       --url "http://kong:8001/consumers/$username/basic-auth" \
       --data "username=$username" \
       --data "password=$password" > /dev/null
}

echo "Register deregnet service"
curl --silent -X POST \
     --url http://kong:8001/services \
     --data 'name=deregnet' \
     --data 'url=http://deregnet-rest:8080/deregnet/' > /dev/null

echo "Register ndex-graphml service"
curl --silent -X POST \
     --url http://kong:8001/services \
     --data 'name=ndex-graphml' \
     --data 'url=http://ndex-graphml:5000/' > /dev/null

echo "Register deregnet docs"
curl --silent -X POST \
     --url http://kong:8001/services \
     --data 'name=deregnet-docs' \
     --data 'url=http://deregnet-docs:5000/' > /dev/null

echo "Register ndex-graphml docs"
curl --silent -X POST \
     --url http://kong:8001/services \
     --data 'name=ndex-graphml-docs' \
     --data 'url=http://ndex-graphml-docs:5000/' > /dev/null

echo "Setting route and path of deregnet service"
curl --silent -X POST \
     --url http://kong:8001/services/deregnet/routes \
     --data 'paths[]=/deregnet' \
     --data 'methods[]=GET' \
     --data 'methods[]=POST' \
     --data 'methods[]=DELETE' > /dev/null

echo "Setting route and path of ndex-graphml service"
curl --silent -X POST \
     --url http://kong:8001/services/ndex-graphml/routes \
     --data 'paths[]=/ndex-graphml' \
     --data 'methods[]=GET' > /dev/null

echo "Setting route and path of deregnet docs"
curl --silent -X POST \
     --url http://kong:8001/services/deregnet-docs/routes \
     --data 'paths[]=/docs/deregnet' \
     --data 'methods[]=GET' > /dev/null

echo "Setting route and path ndex-graphml docs"
curl --silent -X POST \
     --url http://kong:8001/services/ndex-graphml-docs/routes \
     --data 'paths[]=/docs/ndex-graphml' \
     --data 'methods[]=GET' > /dev/null

# TODO: anonymous access?

echo "Enabling basic-auth for deregnet service"
curl --silent -X POST \
     --url http://kong:8001/services/deregnet/plugins \
     --data "name=basic-auth" \
     --data "config.hide_credentials=true" > /dev/null

echo "Enabling basic-auth for ndex-graphml service"
curl --silent -X POST \
     --url http://kong:8001/services/ndex-graphml/plugins \
     --data "name=basic-auth" \
     --data "config.hide_credentials=true" > /dev/null

if [ $ENV == "development" ]; then
  echo "Adding some test user test:test"
  add_consumer 'test' 'test' 
  echo "Adding some test user user:password"
  add_consumer 'user' 'password'
fi
