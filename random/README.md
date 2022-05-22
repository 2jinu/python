# random

다양한 난수를 생성하는 라이브러리

# **INDEX**

**1. [실수 난수 생성](#실수-난수-생성)**

**2. [정수 난수 생성](#정수-난수-생성)**

**3. [선택](#선택)**

**4. [섞기](#섞기)**

**5. [비밀번호 생성기](#비밀번호-생성기)**


# **실수 난수 생성**

실수형 난수를 생성해보자.

```py
import random
print(random.random()) # 0.0 이상 1.0 미만
print(random.uniform(2.0, 5.0)) # 2.0 이상 5.0 미만
```


# **정수 난수 생성**

정수형 난수를 생성해보자.

```py
import random
print(random.randrange(2,5)) # 2 이상 5 미만
print(random.randrange(2,10,2)) # 2,4,6,8 중
print(random.randrange(2,10,3)) # 2,5,8 중
print(random.randrange(5)) # 0 이상 5 미만
print(random.randint(1,5)) # 1 이상 5 이하
```


# **선택**

리스트 데이터에서 랜덤하게 데이터를 선택해보자.

```py
import random
data = [i for i in range(11)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(data))
print(random.sample(data, k=1)) # = [random.choice(data)]
print(random.sample(data, k=2)) # [4, 2], [1, 0], [6, 5], [8, 2], [6, 9], ...
```


# **섞기**

리스트 데이터에서 랜덤하게 데이터를 섞어보자.

```py
import random
data1 = [i for i in range(11)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [i for i in range(11)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(data1)
print(data1) # [8, 9, 2, 3, 7, 1, 10, 6, 5, 0, 4]
print(random.sample(data2, k = len(data2))) # [2, 7, 4, 1, 8, 5, 3, 9, 0, 10, 6]
```


# **비밀번호 생성기**

random을 이용하여 비밀번홍를 생성해보자.

```py
import random
import string

def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation # 영문자 + 숫자 + 문장부호(특수문자)
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

print(get_random_password_string(12))
```