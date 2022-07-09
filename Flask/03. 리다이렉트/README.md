# 리다이렉트

반환 값을 템플릿이 아닌 다른 경로로 리다이렉트

# **INDEX**

**1. [리다이렉트](#리다이렉트)**

# **리다이렉트**

PATH를 지정하여 반환하면 해당 경로로 리다이렉트 된다.

```py
from flask import redirect

@app.route('/redirect1')
def redirect1(): return redirect('/redirected')
```

함수 명을 지정하여 리다이렉트도 가능하다.

```py
from flask import redirect, url_for

@app.route('/redirect2')
def redirect2(): return redirect(url_for('redirect3'))

@app.route('/redirected')
def redirect3(): return 'Hello World'
```