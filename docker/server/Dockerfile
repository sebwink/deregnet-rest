FROM sebwink/deregnet:0.99.999

ARG GUROBI_USER=gurobi

WORKDIR /

COPY server server 
COPY scripts/start_server.sh .
COPY config/docker-config.yml .
COPY requirements.txt .

USER root

RUN apt-get update && \
    apt-get upgrade -y && \
	python3 -m pip install setuptools && \
	python3 -m pip install --no-cache-dir -r requirements.txt

WORKDIR /server

RUN ln -s /server /usr/local/lib/python3.7/dist-packages/deregnet_rest

USER ${GUROBI_USER}

ENTRYPOINT ["/start_server.sh", "--config-file", "/docker-config.yml"]
