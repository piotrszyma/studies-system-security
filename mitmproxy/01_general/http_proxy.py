from mitmproxy import http
from mitmproxy import ctx

from urllib.parse import urlencode

def request(flow: http.HTTPFlow) -> None:
    if 'intercept-request' in flow.request.url:
        flow.request.method = 'GET'
        flow.request.headers['x-request-intercepted'] = 'true'
        flow.request.url += '?' + urlencode({'changeMe': 'Requests are tampered easily'})

