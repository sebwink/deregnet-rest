FROM sebwink/deregnet

WORKDIR /
COPY server server 
COPY scripts/start_server.sh .
COPY config/docker-config.yml .
COPY requirements.txt .

RUN python3 -m pip install pip==18.1
RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install connexion[swagger-ui]
RUN python3 -m pip install elastic-apm[flask]
RUN python3 -m pip install gunicorn 
RUN python3 -m pip install celery

WORKDIR /server

RUN mkdir -p data/db data/graphs data/redis data/runners data/runs data/subgraphs

RUN ln -s /server /usr/local/lib/python3.6/site-packages/deregnet_rest

ENTRYPOINT ["/start_server.sh", "--config-file", "/docker-config.yml"]
