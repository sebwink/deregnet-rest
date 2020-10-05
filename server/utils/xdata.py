import connexion

def consumer_id():
    return connexion.request.headers.get('X-Consumer-ID')
