# python

한줄 쓰기를 통해 python 코드 양을 줄이면서 실행 속도를 높일 수 있다.

# **INDEX**

**1. [if 한줄 쓰기](#if-한줄-쓰기)**

 - [if else 한줄 쓰기](#if-else-한줄-쓰기)

 - [if elif else 한줄 쓰기](#if-elif-else-한줄-쓰기)

**2. [for 한줄 쓰기](#for-한줄-쓰기)**

 - [다중 for 한줄 쓰기](#다중-for-한줄-쓰기)

**3. [for if 한줄 쓰기](#for-if-한줄-쓰기)**

**4. [lambda](#lambda)**

 - [function 한줄 쓰기](#function-한줄-쓰기)

 - [for if와 연동](#for-if와-연동)

 - [filter와 연동](#filter와-연동)


# **if 한줄 쓰기**

if문의 여러 줄을 한줄 쓰기로 바꾸어 해보자.

```py
# 여러 줄
x = 0
if x < 1:
    x = 100

# 한줄
x = 0
if x < 1: x = 100
```


## **if else 한줄 쓰기**

if else 문의 여러 줄을 한줄 쓰기로 바꾸어 해보자.

```py
# 여러 줄
x = 0
if x < 1:
    x = 100
else:
    x = 200

# 한줄
x = 0
x = 100 if x < 1 else 200
```


## **if elif else 한줄 쓰기**

if elif else 문의 여러 줄을 한줄 쓰기로 바꾸어 해보자.

```py
# 여러 줄
x = 0
if x < 1:
    x = 100
elif x == 1:
    x = 200
else:
    x = 300

# 한줄
x = 0
x = 100 if x < 1 else ( 200 if x == 1 else 300 )
```


# **for 한줄 쓰기**

for문의 여러 줄을 한줄 쓰기로 바꾸어 해보자.

```py
# 여러 줄
x = []
for i in range(3):
    x.append(i)

# 한줄
x = [i for i in range(3)]
```


## **다중 for 한줄 쓰기**

중첩된 for문의 여러 줄을 한줄 쓰기로 바꾸어 해보자.

```py
# 여러 줄
x = []
for i in range(3):
    for j in range(3):
        x.append(i * j)

# 한줄
x = [i * j for i in range(3) for j in range(3)]
```


# **for if 한줄 쓰기**

for문과 if문의 여러 줄을 한줄 쓰기로 바꾸어 해보자.

```py
# 여러 줄
x = []
for i in range(3):
    for j in range(3):
        if i > j;
            x.append(i + j)
        else:
            x.append(i - j)

# 한줄
x = [i + j if i > j else i - j for i in range(3) for j in range(3)]
```


# **lambda**

## **function 한줄 쓰기**

간단한 여러 줄의 함수를 lambda를 이용하여 한줄 쓰기로 바꾸어 보자.

```py
# 여러 줄
def my_sum(x, y):
    return x + y

print(my_sum(3, 4))

# 한줄
print((lambda x, y: x + y)(3, 4))
```


## **for if와 연동**

lambda 문법에서 for if을 사용하여 한줄 쓰기로 바꾸어 보자.

```py
# 여러 줄
def my_list(x):
    result = []
    for i in x:
        if i > 0:
            result.append(1)
        else:
            result.append(-1)
    return result

print(my_list([-1, 2, -5, 4]))

# 한줄
print((lambda x : [1 if i > 0 else -1 for i in x])([-1, 2, -5, 4]))
```


## **filter와 연동**

lambda 문법에서 filter를 사용하여 한줄 쓰기로 바꾸어 보자.

```py
# 여러 줄
def my_is_odd(x):
    result = []
    for i in x:
        if i % 2 != 0:
            result.append(i)
    return result

print(my_is_odd([1,2,3]))

# 한줄
print(list(filter(lambda x: x % 2 != 0, [1,2,3])))
```
