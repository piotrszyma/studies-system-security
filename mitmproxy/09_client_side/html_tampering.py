from mitmproxy import http
from mitmproxy import ctx

def request(flow: http.HTTPFlow) -> None:
  if 'task' in flow.request.url:
    flow.request.content = b'QTY=212312331231&Total=0.0'
