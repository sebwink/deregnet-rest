DEREGNET_CONTAINER_ID=$(shell docker images -q sebwink/deregnet)

_IMAGES=deregnet-rest deregnet-worker deregnet-kong-setup deregnet-kong-teardown
IMAGES=$(patsubst %, sebwink/%, $(_IMAGES))

COMPOSE=docker/compose
DOCKER_COMPOSE=docker-compose --project-directory $(COMPOSE)
DEREGNET_BASE=-f $(COMPOSE)/deregnet.base.yml
DEREGNET_DEV=$(DEREGNET_BASE) -f $(COMPOSE)/deregnet.dev.yml
DEREGNET_WORKER_BASE=-f $(COMPOSE)/deregnet-worker.base.yml 
DEREGNET_WORKER_DEV=$(DEREGNET_WORKER_BASE) -f $(COMPOSE)/deregnet-worker.dev.yml
DEREGNET_KONG_SETUP=-f $(COMPOSE)/deregnet.kong-setup.yml
DEREGNET_KONG_TEARDOWN=-f $(COMPOSE)/deregnet.kong-teardown.yml

.PHONY: deregnet

all: $(_IMAGES)

deregnet:
	echo "deregnet"
ifeq ($(DEREGNET_CONTAINER_ID),)
	git submodule update --init --recursive
	cd upstream/deregnet && git pull origin master && make -f docker.mak
endif

deregnet-kong-setup:
	$(DOCKER_COMPOSE) $(DEREGNET_KONG_SETUP) build

deregnet-kong-teardown:
	$(DOCKER_COMPOSE) $(DEREGNET_KONG_TEARDOWN) build

deregnet-rest: deregnet 
	$(DOCKER_COMPOSE) $(DEREGNET_BASE) build 

deregnet-worker: 
	docker-compose -f docker/compose/deregnet-worker.base.yml build $@

% : 
	$(BUILD) $@

up: deregnet 
	$(DOCKER_COMPOSE) $(DEREGNET_DEV) up

down:  
	$(DOCKER_COMPOSE) $(DEREGNET_DEV) rm --stop --force

kong-setup: deregnet
	$(DOCKER_COMPOSE) $(DEREGNET_KONG_SETUP) up
	$(DOCKER_COMPOSE) $(DEREGNET_KONG_SETUP) rm --stop --force

kong-teardown:
	$(DOCKER_COMPOSE) $(DEREGNET_KONG_TEARDOWN) up
	$(DOCKER_COMPOSE) $(DEREGNET_KONG_TEARDOWN) rm --stop --force

kong-up: kong-setup up 
	echo "Started service and executed KONG setup."

kong-down: kong-teardown down
	echo "Stopped service and executed KONG teardown."

worker:
	docker run --rm sebwink/deregnet-worker 
	# scripts/start_worker.sh 
	
worker-down:
	echo "worker-down"

rmi:
	docker rmi $(IMAGES)
