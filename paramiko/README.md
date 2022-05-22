# python

paramiko : SSH2 연결 (클라이언트 또는 서버)을 만들기위한 라이브러리
scp : paramiko 전송을 사용하여 scp 프로토콜을 통해 파일을 보내고 받는 모듈

# **INDEX**

**1. [SSH 접속](#SSH-접속)**

**2. [OS Command](#OS-Command)**
 
 - [foreground](#foreground)

 - [background](#background)

**3. [SCP](#SCP)**

 - [File Upload](#File-Upload)

 - [File Download](#File-Download)


# **SSH 접속**

paramiko를 이용하여 SSH Client를 생성한다.

```py
import paramiko
from scp import SCPClient, SCPException

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.0.58', username='root', password='root')
ssh_client.close()
```


# **OS Command**

## **foreground**

OS Command를 입력하고 결과값을 받자.

```py
stdin, stdout, stderr = ssh_client.exec_command('ip addr')
print(stdout.readlines())
ssh_client.close()
```

## **background**

OS Command를 백그라운드로 실행시켜 보자.

```py
channel = ssh_client.get_transport().open_session()
channel.exec_command('ip addr')
channel.close()
ssh_client.close()
```

# **SCP**

## **File Upload**

Client에서 Server로 파일을 업로드해 보자.

```py
try:
    with SCPClient(ssh_client.get_transport()) as scp:
        scp.put('C:\\Users\\admin\\Downloads\\Hello World.txt', '/root/Hello World.txt', preserve_times=True)
except SCPException:
    raise SCPException.message
```


## **File Download**

Sever에서 Client로 파일을 다운받아 보자.

```py
try:
    with SCPClient(ssh_client.get_transport()) as scp:
        scp.get('/root/Hello World.txt', 'C:\\Users\\admin\\Downloads\\Hello World.txt')
except SCPException:
    raise SCPException.message
```