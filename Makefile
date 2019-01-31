DEREGNET_CONTAINER_ID = $(shell docker images -q sebwink/deregnet)
NDEX_GRAPHML_CONTAINER_ID = $(shell docker images -q sebwink/ndex-graphml)

all: deregnet-rest kong deregnet-kong-setup

deregnet-rest: deregnet
	docker-compose build deregnet-rest 

.PHONY: deregnet

deregnet: 
ifeq ($(DEREGNET_CONTAINER_ID),)
	git submodule update --init --recursive
	cd deregnet && make -f docker.mak
else
	echo "deregnet container already build."
endif

.PHONY: ndex-graphml

ndex-graphml: 
ifeq ($(NDEX_GRAPHML_CONTAINER_ID),)
	git submodule update --init --recursive
	cd ndex-graphml && make
else
	echo "ndex-graphml container already build."
endif

kong:
kong:
	docker-compose build kong 

deregnet-kong-setup:
	docker-compose build deregnet-kong-setup

deploy: deregnet-rest ndex-graphml
	docker-compose -f docker-compose.yml -f docker-compose.deploy.yml up

.PHONY: test

test: 
	docker-compose -f docker-compose.test.yml build 
	docker run --network deregnetrest_default --link deregnetrest_kong_1:kong --rm sebwink/deregnet-rest-test 

clean:
	docker volume prune
