import datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header

import jwt, os, dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

secret = os.getenv("secret")
refresh_secret = os.getenv("refresh_secret")

def decode_token(request):
	auth = get_authorization_header(request).split()

	if auth and len(auth) == 2:
		payload = auth[1].decode('utf-8')
		token = jwt.decode(payload, secret, algorithms='HS256')
		return token['id']

def create_token(id, duration):
	return jwt.encode({
        'id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=duration),
        'iat': datetime.datetime.utcnow()
	}, secret, algorithm='HS256')

def decode_refresh_token(payload):
	token = jwt.decode(payload, secret, algorithms='HS256')
	return token['id']

	
	