# 데코레이터

함수가 실행되기 전 먼저 실행되는 꾸며주는 함수

# **INDEX**

**1. [데코레이터](#데코레이터)**

**2. [에러 핸들링](#에러-핸들링)**

# **데코레이터**

여러 예제에서 사용한 @app.route()가 데코레이터이다.

그 외에 여러 내장 데코레이터가 존재한다.

| Decorator             | Description   |
| :---                  | :---          |
| before_first_request  | flask 실행 후 가장 첫번째 요청에 대해 실행 |
| before_request        | 요청이 있을 때마다 실행 |
| after_request         | 요청에 대한 처리가 끝난 후 클라이언트에 응답 전 실행 |
| teardown_request      | 요청에 대한 처리가 끝난 후 클라이언트에 응답 후 실행 |
| template_filter()     | 템플릿에서 호출 시 실행 |
| errorhandler()        | 서버의 응답 코드에 대해 실행 |

# **에러 핸들링**

errorhandler 데코레이터를 이용하여 사용자 정의 404, 500페이지를 설정한다.

```py
@app.errorhandler(404)
def handle404(error): return "404 Not Found T.T", 404

@app.errorhandler(500)
def handle500(error): return "500 Server Internal Error T.T", 500
```