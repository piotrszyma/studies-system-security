import base64
import code
import javaobj

b64_string = 'rO0ABXQAVklmIHlvdSBkZXNlcmlhbGl6ZSBtZSBkb3duLCBJIHNoYWxsIGJlY29tZSBtb3JlIHBvd2VyZnVsIHRoYW4geW91IGNhbiBwb3NzaWJseSBpbWFnaW5l'
decoded = base64.b64decode(b64_string)

loaded_obj = javaobj.loads(decoded)