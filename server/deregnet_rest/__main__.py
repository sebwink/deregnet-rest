#!/usr/bin/env python3

import os

from elasticapm.contrib.flask import ElasticAPM

from deregnet_rest import app
from deregnet_rest.init import config

DEBUG = not bool(os.getenv('DEPLOY', False))

app.app.config['ELASTIC_APM'] = {
    # Set required service name. Allowed characters:
    # a-z, A-Z, 0-9, -, _, and space
    'SERVICE_NAME': 'deregnet-rest',
    # Set custom APM Server URL (default: http://localhost:8200)
    'SERVER_URL': 'http://apm-server:8200',
    'DEBUG': DEBUG,
}

apm = ElasticAPM(app.app)

if __name__ == '__main__':
    app.run(host=config.host,
            port=config.port,
            debug=DEBUG,
            server=config.server_backend)
