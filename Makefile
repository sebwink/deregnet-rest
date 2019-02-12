DEREGNET_CONTAINER_ID = $(shell docker images -q sebwink/deregnet)
NDEX_GRAPHML_CONTAINER_ID = $(shell docker images -q sebwink/ndex-graphml)

COMPOSE=docker/compose
NETWORK=-f $(COMPOSE)/network.yml
DOCKER_COMPOSE=docker-compose $(NETWORK)
DEREGNET_BASE=-f $(COMPOSE)/deregnet.base.yml
DEREGNET_DEV=$(DEREGNET_BASE) -f $(COMPOSE)/deregnet.dev.yml
POSTGRES_BASE=-f $(COMPOSE)/postgres.base.yml
POSTGRES_DEV=$(POSTGRES_BASE) -f $(COMPOSE)/postgres.dev.yml
MONGODB_BASE=-f $(COMPOSE)/mongodb.base.yml 
MONGODB_DEV=$(MONGODB_BASE) -f $(COMPOSE)/mongodb.dev.yml
REDIS_BASE=-f $(COMPOSE)/redis.base.yml 
REDIS_DEV=$(REDIS_BASE) -f $(COMPOSE)/redis.dev.yml

all: deregnet-rest kong deregnet-kong-setup

.PHONY: deregnet

deregnet: 
ifeq ($(DEREGNET_CONTAINER_ID),)
	git submodule update --init --recursive
	cd upstream/deregnet && make -f docker.mak
else
	echo "deregnet container already build."
endif

.PHONY: ndex-graphml

ndex-graphml: 
ifeq ($(NDEX_GRAPHML_CONTAINER_ID),)
	git submodule update --init --recursive
	cd upstream/ndex-graphml && make
else
	echo "ndex-graphml container already build."
endif

kong:
	docker-compose build kong 

deploy: deregnet-rest ndex-graphml
	docker-compose -f docker-compose.yml -f docker-compose.deploy.yml up

.PHONY: deregnet-network network

deregnet-network:
	docker network create deregnet

network: deregnet-network

deregnet-kong-setup:
	docker-compose -f docker/compose/deregnet.base.yml \
                   -f docker/compose/deregnet.dev.yml \
				   -f docker/compose/mongodb.base.yml \
				   -f docker/compose/postgres.base.yml build deregnet-kong-setup


deregnet-rest: deregnet
	$(DOCKER_COMPOSE) $(DEREGNET_BASE) $(MONGODB_BASE) $(REDIS_BASE) $(POSTGRES_BASE) build $@

dev:
	$(DOCKER_COMPOSE) $(DEREGNET_DEV) $(POSTGRES_DEV) $(MONGODB_DEV) $(REDIS_DEV) up
                   

dev-down: 
	$(DOCKER_COMPOSE) $(DEREGNET_DEV) $(POSTGRES_DEV) $(MONGODB_DEV) $(REDIS_DEV) down

.PHONY: test

test: 
	docker-compose -f docker-compose.test.yml build 
	docker run --network deregnetrest_default --link deregnetrest_kong_1:kong --rm sebwink/deregnet-rest-test 

clean:
	docker volume prune
