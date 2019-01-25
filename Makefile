all: deregnet-rest kong deregnet-kong-setup

deregnet-rest:
	./compose.sh build deregnet-rest 
kong:
	./compose.sh build kong 
deregnet-kong-setup:
	./compose.sh build deregnet-kong-setup
