#!/usr/bin/env xonsh

def registerNdexGraphmlService():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services \
             --data 'name=ndex-graphml' \
             --data 'url=http://ndex-graphml:5000/'
    )

def registerNdexGraphmlDocumentation():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services \
             --data 'name=ndex-graphml-docs' \
             --data 'url=http://ndex-graphml-docs:5000/'
    )

def registerNdexGraphmlRoute():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/ndex-graphml/routes \
             --data 'paths[]=/ndex-graphml' \
             --data 'methods[]=GET'
    )

def registerNdexGraphmlDocumentationRoute():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/ndex-graphml-docs/routes \
             --data 'paths[]=/docs/ndex-graphml' \
             --data 'methods[]=GET'
    )

def enableBasicAuthForNdexGraphml():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/ndex-graphml/plugins \
             --data "name=basic-auth" \
             --data "config.hide_credentials=true"
    )

if __name__ == '__main__':
    registerNdexGraphmlService()
    registerNdexGraphmlRoute()
    enableBasicAuthForNdexGraphml()
    registerNdexGraphmlDocumentation()
    registerNdexGraphmlDocumentationRoute()
