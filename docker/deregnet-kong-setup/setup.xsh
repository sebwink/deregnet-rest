#!/usr/bin/env xonsh

import json 

def loadsJson(f):

    def _f(*args, **kwargs):
        ret = f(*args, **kwargs)
        return json.loads(ret)

    return _f

@loadsJson
def registerDeregnetService():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services \
             --data 'name=deregnet' \
             --data 'url=http://deregnet-rest:8080/deregnet/'
    )


@loadsJson 
def registerDeregnetServiceRoute():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/deregnet/routes \
			 --data 'name=deregnet' \
             --data 'paths[]=/deregnet' \
             --data 'methods[]=GET' \
             --data 'methods[]=POST' \
             --data 'methods[]=DELETE'
    )

@loadsJson 
def enableJwtForDeregnetService():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/deregnet/plugins \
             --data "name=jwt"
    )

@loadsJson 
def registerDeregnetDocumentation():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services \
             --data 'name=deregnet-docs' \
             --data 'url=http://deregnet-docs:5000/'
    )

@loadsJson 
def registerDeregnetDocumentationRoute():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/deregnet-docs/routes \
             --data 'paths[]=/docs/deregnet' \
             --data 'methods[]=GET'
    )

if __name__ == '__main__':
    # DeRegNet service
    registerDeregnetService()
    registerDeregnetServiceRoute()
    enableJwtForDeregnetService()
    # DeRegNet documentation
    #registerDeregnetDocumentation()
    #registerDeregnetDocumentationRoute()
