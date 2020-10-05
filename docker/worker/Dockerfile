FROM sebwink/deregnet:0.99.999

WORKDIR /

COPY server server 
COPY scripts/start_worker.sh .
COPY config/docker-config.yml .
COPY requirements.txt .

RUN apt-get update && \
    apt-get upgrade -y && \
	python3 -m pip install setuptools && \
	python3 -m pip install --no-cache-dir -r requirements.txt

WORKDIR /server

RUN ln -s /server /usr/local/lib/python3.7/site-packages/deregnet_rest

CMD ["/start_worker.sh", "--config-file", "/docker-config.yml"]
