#!/usr/bin/env xonsh

def registerKonga():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services \
             --data 'name=konga' \
             --data 'url=http://konga:1337/'
    )

def registerKongaRoute():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/konga/routes \
             --data 'paths[]=/admin/konga'
    )

if __name__ == '__main__':
	registerKonga()
	registerKongaRoute()
