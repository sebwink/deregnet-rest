DEREGNET_CONTAINER_ID=$(shell docker images -q sebwink/deregnet)
DEREGNET_NETWORK=$(shell docker network ls | grep deregnet) 

COMPOSE=docker/compose
NETWORK=-f $(COMPOSE)/network.yml
DOCKER_COMPOSE=docker-compose $(NETWORK)
KONG_BASE=-f $(COMPOSE)/kong.base.yml 
KONG_DEV=$(KONG_BASE) -f $(COMPOSE)/kong.dev.yml
DEREGNET_BASE=-f $(COMPOSE)/deregnet.base.yml
DEREGNET_DEV=$(DEREGNET_BASE) -f $(COMPOSE)/deregnet.dev.yml
POSTGRES_BASE=-f $(COMPOSE)/postgres.base.yml
POSTGRES_DEV=$(POSTGRES_BASE) -f $(COMPOSE)/postgres.dev.yml
MONGODB_BASE=-f $(COMPOSE)/mongodb.base.yml 
MONGODB_DEV=$(MONGODB_BASE) -f $(COMPOSE)/mongodb.dev.yml
REDIS_BASE=-f $(COMPOSE)/redis.base.yml 
REDIS_DEV=$(REDIS_BASE) -f $(COMPOSE)/redis.dev.yml
ELK_BASE=-f $(COMPOSE)/elk.base.yml
ELK_DEV=$(ELK_BASE) -f $(COMPOSE)/elk.dev.yml

BUILD=$(DOCKER_COMPOSE) $(KONG_BASE) $(DEREGNET_BASE) $(MONGODB_BASE) $(REDIS_BASE) $(POSTGRES_BASE) build
DEV=$(DOCKER_COMPOSE) $(KONG_BASE) $(DEREGNET_DEV) $(POSTGRES_DEV) $(MONGODB_DEV) $(REDIS_DEV)

_CONTAINERS=deregnet-rest deregnet kong kong-auth kong-ssl kong-admin-api konga-setup deregnet-docs kong-auth-setup
CONTAINERS=$(patsubst %, sebwink/%, $(_CONTAINERS))

.PHONY: deregnet deregnet-network

deregnet-network:
ifeq ($(DEREGNET_NETWORK),)
	docker network create deregnet 
else
	echo "deregnet network already created."   
endif

network: deregnet-network

deregnet: 
ifeq ($(DEREGNET_CONTAINER_ID),)
	git submodule update --init --recursive
	cd upstream/deregnet && make -f docker.mak
else
	echo "deregnet container already build."
endif

deregnet-rest: network
	$(BUILD) $@

deregnet-worker: deregnet-rest
	docker-compose -f docker/compose/deregnet.worker.yml build $@

deregnet-docs: network
	$(BUILD) $@

deregnet-kong-setup: network
	$(BUILD) $@

kong: network
	$(BUILD) $@ 

kong-admin-api: network
	$(BUILD) $@

kong-ssl: network
	$(BUILD) $@

kong-auth: network 
	$(BUILD) $@

kong-auth-setup: network 
	$(BUILD) $@

setup-konga: network
	$(BUILD) $@

up: network deregnet 
	$(DEV) up

down: network 
	$(DEV) down

elk-dev: network
	$(DOCKER_COMPOSE) $(ELK_DEV) up

elk-dev-down: network
	$(DOCKER_COMPOSE) $(ELK_DEV) down

worker-dev:
	scripts/start_worker.sh

rmi:
	docker rmi $(CONTAINERS)

clean:
	docker volume prune
