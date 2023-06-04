from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header

import jwt, os, dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

def decode_token(request):
	auth = get_authorization_header(request).split()

	if auth and len(auth) == 2:
		payload = auth[1].decode('utf-8')
		secret = os.getenv("secret")
		token = jwt.decode(payload, secret, algorithms='HS256')
		return token['id']
