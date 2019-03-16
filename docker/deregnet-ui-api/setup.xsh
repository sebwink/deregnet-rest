#!/usr/bin/env xonsh

import json 

def loadsJson(f):

    def _f(*args, **kwargs):
        ret = f(*args, **kwargs)
        return json.loads(ret)

    return _f

@loadsJson
def registerDeregnetUiApiService():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services \
             --data 'name=deregnet-ui-api' \
             --data 'url=http://deregnet-rest:8080/deregnet/'
    )


@loadsJson 
def registerDeregnetUiApiServiceRoute():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/deregnet-ui-api/routes \
             --data 'paths[]=/api/ui' \
             --data 'methods[]=GET' \
             --data 'methods[]=POST' \
             --data 'methods[]=DELETE'
    )

@loadsJson 
def enableJwtForDeregnetUiApiService():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/deregnet-ui-api/plugins \
             --data "name=jwt"
    )

@loadsJson 
def enableCookieJwtForDeregnetUiApiService():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/deregnet-ui-api/plugins \
             --data "name=cookie_jwt" \
             --data "config.cookie_names[]=session"
    )

if __name__ == '__main__':
    # DeRegNet UI API service
    registerDeregnetUiApiService()
    registerDeregnetUiApiServiceRoute()
    enableJwtForDeregnetUiApiService()
    enableCookieJwtForDeregnetUiApiService()
