#!/usr/bin/env xonsh

def registerKongAdminApi():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services \
             --data 'name=kong-admin' \
             --data 'url=http://localhost:8001/'
    )

def registerKongAdminApiRoute():
    return $(
        curl --silent -X POST \
             --url http://kong:8001/services/kong-admin/routes \
             --data 'paths[]=/kong' \
             --data 'methods[]=GET'
    )


def enableKeyAuthForKongAdminApi():
	return $(
		curl --silent -X POST \
             --url http://kong:8001/services/kong-admin/plugins \
             --data "name=key-auth"
	)

def registerAdminUser():
    adminUser = $(
        curl --silent -X POST \
              --url http://kong:8001/consumers \
              --data @('username='+$KONG_ADMIN_USER)
    )
    adminKey = $(
        curl --silent -X POST \
             --url @("http://kong:8001/consumers/{}/key-auth".format($KONG_ADMIN_USER))
    )
    return adminUser, adminKey

if __name__ == '__main__':
	registerKongAdminApi()
	registerKongAdminApiRoute()
	enableKeyAuthForKongAdminApi()
	registerAdminUser()
