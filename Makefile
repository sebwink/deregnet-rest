all: deregnet-rest kong deregnet-kong-setup

deregnet-rest:
	docker-compose build deregnet-rest 
kong:
	docker-compose build kong 
deregnet-kong-setup:
	docker-compose build deregnet-kong-setup

deploy: deregnet-rest
	docker-compose -f docker-compose.yml -f docker-compose.deploy.yml up
