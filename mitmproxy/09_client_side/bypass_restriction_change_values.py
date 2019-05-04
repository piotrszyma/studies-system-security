from mitmproxy import http
from mitmproxy import ctx

def request(flow: http.HTTPFlow) -> None:
  if 'FieldRestriction' in flow.request.url:
    flow.request.content = b'select=lorem&radio=ipsum&checkbox=dolor&shortInput=heheeheheeheheh'