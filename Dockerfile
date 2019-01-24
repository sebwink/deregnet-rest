FROM sebwink/deregnet

WORKDIR /
COPY server server
WORKDIR /server

RUN python3 -m pip install pip==18.1
RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install connexion[swagger-ui]

RUN mkdir -p data/db data/graphs data/redis data/runners data/runs data/subgraphs

RUN ln -s /server/deregnet_rest /usr/local/lib/python3.6/site-packages/deregnet_rest

ENTRYPOINT ["./start_server.sh", "--config-file", "docker-config.yml"]
