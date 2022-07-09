# 세션

쿠키에 데이터를 암호화하여 저장

# **INDEX**

**1. [세션](#세션)**

# **세션**

secrets모듈이나 os.urandom으로 난수를 생성한 뒤 비밀키로 설정한다.

```py
import secrets

app.secret_key = secrets.token_hex(16)
```

비밀키를 설정하였다면 세션을 생성할 수 있다.

```py
from flask import session

@app.route('/login/')
def login():
    session['user'] = 'John Doe'
    return 'Session Created'
```

dictionary처럼 세션 값들을 조회할 수 있다.

```py
@app.route('/auth/')
def auth():
    if 'user' in session: return "Hello {}".format(session['user'])
```

세션은 전체 삭제하거나 특정 키만 삭제할 수 있다.

```py
@app.route('/logout/')
def logout():
    session.clear()
    return 'Logout'

@app.route('/pop/')
def pop():
    session.pop('user', None)
    return 'Pop'
```