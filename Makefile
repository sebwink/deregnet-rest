DEREGNET_CONTAINER_ID=$(shell docker images -q sebwink/deregnet)
DEREGNET_NETWORK=$(shell docker  ls | grep deregnet) 

COMPOSE=docker/compose
DOCKER_COMPOSE=docker-compose
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
DEV=$(DOCKER_COMPOSE) $(KONG_DEV) $(DEREGNET_DEV) $(POSTGRES_DEV) $(MONGODB_DEV) $(REDIS_DEV)

_CONTAINERS=deregnet-rest deregnet kong kong-auth kong-ssl kong-admin-api konga-setup deregnet-docs kong-auth-setup
CONTAINERS=$(patsubst %, sebwink/%, $(_CONTAINERS))

.PHONY: deregnet deregnet-

deregnet: 
ifeq ($(DEREGNET_CONTAINER_ID),)
	git submodule update --init --recursive
	cd upstream/deregnet && git pull origin master && make -f docker.mak
else
	echo "deregnet container already build."
endif

deregnet-rest: deregnet
	$(BUILD) $@

deregnet-worker: 
	docker-compose -f docker/compose/deregnet.worker.yml build $@

deregnet-docs: 
	$(BUILD) $@

deregnet-kong-setup: 
	$(BUILD) $@

deregnet-ui-api-kong-setup: 
	$(BUILD) $@

kong: 
	$(BUILD) $@ 

kong-admin-api: 
	$(BUILD) $@

kong-ssl: 
	$(BUILD) $@

kong-auth:  
	$(BUILD) $@

kong-auth-setup:  
	$(BUILD) $@

setup-konga: 
	$(BUILD) $@

up:  deregnet 
	$(DEV) up

down:  
	$(DEV) down

elk-dev: 
	$(DOCKER_COMPOSE) --project-directory $(COMPOSE) $(ELK_DEV) up

elk-dev-down: 
	$(DOCKER_COMPOSE) --project-directory $(COMPOSE) $(ELK_DEV) down

worker:
	scripts/start_worker.sh

rmi:
	docker rmi $(CONTAINERS)

clean:
	docker volume prune
