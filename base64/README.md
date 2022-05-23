# base64

# **INDEX**

**1. [Encoding](#Encoding)**

**2. [Decoding](#Decoding)**


# **Encoding**

읽을 수 있는 문자열을 base64로 인코딩 해보자.

```py
import base64
text = 'Hello World!!!'
encoded = base64.b64encode(text.encode())
print(encoded)
```


# **Decoding**

base64 문자열을 읽을 수 있는 문자열로 디코딩 해보자.

```py
import base64
decoded = base64.b64decode(b'SGVsbG8gV29ybGQhISE=')
print(decoded.decode())
```