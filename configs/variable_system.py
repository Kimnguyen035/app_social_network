KEY_RSA = 'duanfpro'

U = 'username'
P = 'password'

TOKEN = {
    'private_key':'anphMNcZkh',
    'public_key':'fnEcdMHkm',
    'type':'Bearer ',
    'hash':'HS256',
    'tls_access_token':60*60,
    'tls_refresh_token':60*60*3
}

GROUP_URL = {
    'url_auth',
}

THROTTLING = {
        'rate': '1',
        'split': '/',
        'waiting_time': 3,
        'type_time': 's',
        'method': [
            'GET'
        ],
}