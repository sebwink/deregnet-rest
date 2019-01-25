import connexion

from deregnet_rest import encoder


app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml',
            arguments={'title': 'DeRegNet REST API'})
