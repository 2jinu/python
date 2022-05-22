# 환경 확인

python을 이용하여 현재 운영체제, python 버전 등을 확인

# **INDEX**

**1. [실행 환경 확인](#실행-환경-확인)**


# **실행 환경 확인**

현재 디렉토리, 운영체제 등 확인할 수 있다.

```py
import sys
import platform
import os

print(os.getcwd())             # 작업 위치
print(platform.architecture()) # bit
print(platform.system())       # platform
print(sys.version)             # python 버전
print(sys.executable)          # python 설치 위치
```