# python

URL 작업을 위한 여러 모듈을 모은 패키지

# **INDEX**

**1. [URL parsing](#URL-parsing)**

**2. [GET request](#GET-request)**

**3. [POST request](#POST-request)**


# **URL parsing**

URL 문자열을 쪼개볼 수 있다.

```py
import urllib
url_parser = urllib.parse.urlparse('https://www.google.com/webhp?hl=ko&sa=X&ved=0ahUKEwih1MWkiv_sAhXKfXAKHZI6DkgQPAgI')
print('{:<15} : {}'.format('scheme',url_parser.scheme))
print('{:<15} : {}'.format('netloc',url_parser.netloc))
print('{:<15} : {}'.format('path',url_parser.path))
print('{:<15} : {}'.format('params',url_parser.params))
print('{:<15} : {}'.format('query',url_parser.query))
print('{:<15} : {}'.format('fragment',url_parser.fragment))
```


# **GET request**

urllib를 이용하여 GET 요청을 보낼 수 있다.

```py
import urllib
import urllib.request
url     = 'https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 'Content-Type': 'application/json; charset=utf-8'}
request = urllib.request.Request(url, headers = headers)

try:
    response= urllib.request.urlopen(request)
    print(response.status)
    print(response.read().decode())
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
except urllib.error.URLError as e:
    print(e.reason)
```


# **POST request**

urllib를 이용하여 POST 요청을 보낼 수 있다.

```py
import urllib
import urllib.request
url     = 'https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
params  = urllib.parse.urlencode({'id':'1234'}).encode('utf-8')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 'Content-Type': 'application/x-www-form-urlencoded'}
request = urllib.request.Request(url, headers = headers, data = params)

try:
    response= urllib.request.urlopen(request, data=params)
    print(response.status)
    print(response.read().decode())
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
except urllib.error.URLError as e:
    print(e.reason)
```