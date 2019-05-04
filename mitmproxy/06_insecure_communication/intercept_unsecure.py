from mitmproxy import http
from mitmproxy import ctx

def request(flow: http.HTTPFlow) -> None:
  if 'start' in flow.request.url:
    print('Intercepted credentials')
    print(flow.request.content)
