#!/usr/bin/env python3

import connexion

from deregnet_rest import encoder
from deregnet_rest.init import config

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml',
                arguments={'title': 'DeRegNet REST API'})
    app.run(host=config.host,
            port=config.port,
            debug=config.debug,
            server=config.server_backend)


if __name__ == '__main__':
    main()
