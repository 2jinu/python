# base64

8비트 이진 데이터를 문자 코드에 영향을 받지 않는 공통 ASCII 영역의 문자들로만 이루어진 일련의 문자열로 바꾸는 인코딩 방식

# **INDEX**

**1. [Encoding](#Encoding)**

**2. [Decoding](#Decoding)**


# **Encoding**

읽을 수 있는 문자열을 base64로 인코딩 해보자.

```py
import base64
text = 'Hello World!!!'
encoded = base64.b64encode(text.encode())
print('{:<20} : {}'.format('Before', text))
print('{:<20} : {}'.format('After', encoded))
```


# **Decoding**

base64 문자열을 읽을 수 있는 문자열로 디코딩 해보자.

```py
import base64
decoded = base64.b64decode(b'SGVsbG8gV29ybGQhISE=')
print('{:<20} : {}'.format('Before', b'SGVsbG8gV29ybGQhISE='))
print('{:<20} : {}'.format('After', decoded.decode()))
```