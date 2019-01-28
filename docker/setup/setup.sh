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

echo "Setting route and path of deregnet service"
curl --silent -X POST \
     --url http://kong:8001/services/deregnet/routes \
     --data 'paths[]=/deregnet' \
     --data 'methods[]=GET' \
     --data 'methods[]=POST' \
     --data 'methods[]=DELETE' > /dev/null

# TODO: anonymous access?

echo "Enabling basic-auth for deregnet service"
curl --silent -X POST \
     --url http://kong:8001/services/deregnet/plugins \
     --data "name=basic-auth" \
     --data "config.hide_credentials=true" > /dev/null

if [ $ENV == "development" ]; then
  echo "Adding some test user a:a"
  add_consumer 'test' 'test' 
  echo "Adding some test user b:b"
  add_consumer 'user' 'password'
fi
