COMPOSE=docker/compose
DOCKER_COMPOSE=docker-compose --project-directory $(COMPOSE)
# MONGODB (for development purposes)
MONGODB_BASE=-f $(COMPOSE)/mongodb/base.yml
MONGODB_DEV=$(MONGODB_BASE) -f $(COMPOSE)/mongodb/dev.yml
# REDIS (for development purposes)
REDIS_BASE=-f $(COMPOSE)/redis/base.yml
REDIS_DEV=$(REDIS_BASE) -f $(COMPOSE)/redis/dev.yml
# DEREGNET SERVER
DEREGNET_SERVER_BASE=-f $(COMPOSE)/deregnet/server.base.yml
DEREGNET_SERVER_DEV=$(DEREGNET_SERVER_BASE) -f $(COMPOSE)/deregnet/server.dev.yml

ALL_DEV=$(MONGODB_DEV) $(REDIS_DEV) $(DEREGNET_SERVER_DEV)

up: up@dev
	@#

up@dev: server@dev
	@#

down: down@dev
	@#

down@dev: 
	@$(DOCKER_COMPOSE) $(ALL_DEV) down

mongo@dev:
	@$(DOCKER_COMPOSE) $(MONGODB_DEV) up -d

redis@dev:
	@$(DOCKER_COMPOSE) $(REDIS_DEV) up -d

server-image:
	@$(DOCKER_COMPOSE) $(DEREGNET_SERVER_BASE) build

server: server@dev
	@#

server@dev: server-image mongo@dev redis@dev
	@$(DOCKER_COMPOSE) $(DEREGNET_SERVER_DEV) up -d
