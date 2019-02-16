FROM sebwink/deregnet-rest

COPY scripts/start_worker.sh /

ENTRYPOINT ["/start_worker.sh", "--config-file", "/docker-config.yml"]
