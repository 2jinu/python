import base64
decoded = base64.b64decode(b'SGVsbG8gV29ybGQhISE=')
print('{:<20} : {}'.format('Before', b'SGVsbG8gV29ybGQhISE='))
print('{:<20} : {}'.format('After', decoded.decode()))