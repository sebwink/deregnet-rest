DEREGNET_CONTAINER_ID = $(shell docker images -q sebwink/deregnet)

all: deregnet-rest kong deregnet-kong-setup

deregnet-rest: deregnet
	docker-compose build deregnet-rest 

.PHONY: deregnet

deregnet: 
ifeq ($(DEREGNET_CONTAINER_ID),)
	cd deregnet && make -f docker.mak
else
	echo "deregnet container already build."
endif

kong:
	docker-compose build kong 

deregnet-kong-setup:
	docker-compose build deregnet-kong-setup

deploy: deregnet-rest
	docker-compose -f docker-compose.yml -f docker-compose.deploy.yml up
