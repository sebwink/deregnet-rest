FROM sebwink/deregnet

WORKDIR /

COPY server server 
COPY scripts/start_server.sh .
COPY config/docker-config.yml .
COPY requirements.txt .

RUN apt-get update && \
    apt-get upgrade -y && \
	python3 -m pip install setuptools && \
	python3 -m pip install --no-cache-dir -r requirements.txt

WORKDIR /server

RUN ln -s /server /usr/local/lib/python3.5/dist-packages/deregnet_rest

ENTRYPOINT ["/start_server.sh", "--config-file", "/docker-config.yml"]
