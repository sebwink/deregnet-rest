#!/usr/bin/env python3

import os
import connexion
from elasticapm.contrib.flask import ElasticAPM
from deregnet_rest import encoder
from deregnet_rest.config import Config

DEBUG = not bool(os.getenv('DEPLOY', False))

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'DeRegNet REST API'})
    app.app.config['ELASTIC_APM'] = {
        # Set required service name. Allowed characters:
        # a-z, A-Z, 0-9, -, _, and space
        'SERVICE_NAME': 'deregnet-rest',
        # Set custom APM Server URL (default: http://localhost:8200)
        'SERVER_URL': 'http://apm-server:8200',
        'DEBUG': DEBUG,
    }
    apm = ElasticAPM(app.app)
    app.run(host=Config.host(),
            port=Config.port(),
            debug=DEBUG,
            server=Config.server_backend())


if __name__ == '__main__':
    main()
