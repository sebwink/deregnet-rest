#!/usr/bin/env xonsh

import json

$KONG='http://kong:8001'

def loadsJson(f):
    
    def _f(*args, **kwargs):
        ret = f(*args, **kwargs)
        return json.loads(ret)

    return _f

@loadsJson
def registerSignupService():
    return $(
        curl --silent -X POST \
             --url $KONG/services \
             --data 'name=signup' \
             --data 'url=http://kong-auth:5000/signup/'
    ) 

@loadsJson
def registerSignupServiceRoute():
    return $(
        curl --silent -X POST \
             --url $KONG/services/signup/routes \
             --data 'paths[]=/signup' 
    )

@loadsJson
def registerAccountService():
    return $(
        curl --silent -X POST \
             --url $KONG/services \
             --data 'name=account' \
             --data 'url=http://kong-auth:5000/consumer/'
    )

@loadsJson
def registerAccountServiceRoute():
    return $(
        curl --silent -X POST \
             --url $KONG/services/account/routes \
             --data 'paths[]=/account'
    )

@loadsJson
def enableBasicAuthOnRoute(routeId):
    return $(
        curl --silent -X POST \ 
             --url $KONG/routes/@(routeId)/plugins \
             --data 'name=basic-auth' \
             --data 'config.hide_credentials=false'
    )

@loadsJson
def registerAccessService():
    return $(
        curl --silent -X POST \
             --url $KONG/services \
             --data 'name=access' \
             --data 'url=http://kong-auth:5000/access/'
    )

@loadsJson
def registerAccessServiceRoute():
    return $(
        curl --silent -X POST \
             --url $KONG/services/access/routes \
             --data 'paths[]=/access'
    )

if __name__ == '__main__':
    # /signup
    registerSignupService()
    registerSignupServiceRoute()
    # /account
    registerAccountService()
    accountRouteId = registerAccountServiceRoute()['id']
    enableBasicAuthOnRoute(accountRouteId)
    # /access
    registerAccessService()
    accessRouteId = registerAccessServiceRoute()['id']
    enableBasicAuthOnRoute(accessRouteId)
