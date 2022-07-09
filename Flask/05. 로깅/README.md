# 로깅

flask내 기본 로그 모듈을 대체하거나 추가 로깅을 설정

# **INDEX**

**1. [기본 로거를 이용한 로깅](#기본-로거를-이용한-로깅)**

**2. [logging](#logging)**

 - [파일에 로그 저장](#파일에-로그-저장)

# **기본 로거를 이용한 로깅**

다음과 같이 flask내 기본 로거를 사용할 수 있다.

```py
from flask import Flask, request

@app.route('/logging/')
def logging_():
    app.logger.debug('Connection : {}'.format(request.remote_addr))
    app.logger.info('Connection : {}'.format(request.remote_addr))
    app.logger.warning('Connection : {}'.format(request.remote_addr))
    app.logger.error('Connection : {}'.format(request.remote_addr))
    app.logger.critical('Connection : {}'.format(request.remote_addr))
    return "Hello World"
```

로깅할 최소 로그레벨을 지정하여 사용할 수 있다.

로그레벨은 다음과 같다.

| Level     | Value |
| :---:     | :---: |
| DEBUG     | 10    |
| INFO      | 20    |
| WARNING   | 30    |
| ERROR     | 40    |
| CRITICAL  | 50    |

```py
app.logger.setLevel(40)
@app.route('/loglevel/')
def loglevel():
    app.logger.warning('Connection : {}'.format(request.remote_addr))
    app.logger.error('Connection : {}'.format(request.remote_addr))
    return "Hello World"
```

# **logging**

기본 로거를 비활성화 한다.

```py
import logging

app.logger = logging.getLogger('werkzeug')
app.logger.disabled = True
```

로그 레벨과 포맷팅을 별도로 설정이 가능하며 아래의 예제에서 method, url과 version은 기본 포맷이 아닌 사용자 정의 포맷이다.

```py
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(name)s] [%(levelname)s] [%(remote_addr)s] \"%(method)s %(url)s %(version)s\" : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
```

로그의 이름을 설정한다.

```py
logger = logging.getLogger('Logger')
```

method, url과 version은 사용자 정의 포맷이라고 하였다. 로그를 기록 시 extra변수를 통해서 사용자 정의 포맷에 데이터를 전달할 수 있다.

```py
def default():
    logger.info("logging...", extra={'remote_addr': request.remote_addr, 'method': request.method, 'url': request.path, 'version': request.environ.get('SERVER_PROTOCOL')})
    logger.error("logging...", extra={'remote_addr': request.remote_addr, 'method': request.method, 'url': request.path, 'version': request.environ.get('SERVER_PROTOCOL')})
    return "Hello World"
```

## **파일에 로그 저장**

아래의 예제에서 logger와 FileLogger는 서로 다른 로거이며 설정 값도 별도로 적용된다.

```py
FileLogger = logging.FileHandler(filename='test.log', mode='a', encoding='utf-8')
FileLogger.setFormatter(fmt=logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] [%(remote_addr)s] \"%(method)s %(url)s %(version)s\" : %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
FileLogger.setLevel(logging.ERROR)
logger.addHandler(FileLogger)

@app.route('/file/')
def file():
    logger.info("logging...", extra={'remote_addr': request.remote_addr, 'method': request.method, 'url': request.path, 'version': request.environ.get('SERVER_PROTOCOL')})
    logger.critical("logging...", extra={'remote_addr': request.remote_addr, 'method': request.method, 'url': request.path, 'version': request.environ.get('SERVER_PROTOCOL')})
    return "Hello World"
```

파일에 저장 시 최대로 저장할 byte와 백업의 개수를 지정하여 로테이팅을 시킬 수 있다.

```py
from logging.handlers import RotatingFileHandler
FileLogger = RotatingFileHandler(filename='test.log', mode='a', maxBytes=10, backupCount=2, encoding='utf-8')
FileLogger.setFormatter(fmt=logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] [%(remote_addr)s] \"%(method)s %(url)s %(version)s\" : %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
FileLogger.setLevel(logging.WARNING)
logger.addHandler(FileLogger)

@app.route('/rotating/')
def rotating():
    logger.debug("logging...", extra={'remote_addr': request.remote_addr, 'method': request.method, 'url': request.path, 'version': request.environ.get('SERVER_PROTOCOL')})
    logger.warning("logging...", extra={'remote_addr': request.remote_addr, 'method': request.method, 'url': request.path, 'version': request.environ.get('SERVER_PROTOCOL')})
    return "Hello World"
```