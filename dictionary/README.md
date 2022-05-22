# dictionary

dictionary는 "키(Key)/값(Value)" 쌍을 요소로 갖는 자료형

# **INDEX**

**1. [선언 방법](#선언-방법)**

**2. [데이터 다루기](#데이터-다루기)**

 - [데이터 읽기](#데이터-읽기)

 - [데이터 추가](#데이터-추가)

 - [데이터 삭제](#데이터-삭제)

 - [데이터 변경](#데이터-변경)

**3. [기타 속성](#기타-속성)**

# **선언 방법**

dict를 통해 선언하거나 "{}"를 통해 선언할 수 있다.

```py
mydict1 = dict()
mydict2 = {}
```

데이터를 넣으면서 선언할 수 있다.

```py
mydict1 = {
    'Name': ['user1', 'user2'],
    'Age' : [20,15],
    'Addr' : ['서울','서울']
    }
mydict2 = dict([
    ('Name',['user1','user2']),
    ('Age',[20,15]),
    ('Addr',['서울','서울'])
    ])
mydict3 = dict(
    Name=['user1','user2'],
    Age=[20,15],
    Addr=['서울','서울']
    )
mydict4 = dict(zip(
    ['Name','Age','Addr'],
    [
        ['user1','user2'],
        [20,15],
        ['서울','서울']
    ]
    ))

print(mydict1)
print(mydict2)
print(mydict3)
print(mydict4)

출력 결과
{'Name': ['user1', 'user2'], 'Age': [20, 15], 'Addr': ['서울', '서울']}
{'Name': ['user1', 'user2'], 'Age': [20, 15], 'Addr': ['서울', '서울']}
{'Name': ['user1', 'user2'], 'Age': [20, 15], 'Addr': ['서울', '서울']}
{'Name': ['user1', 'user2'], 'Age': [20, 15], 'Addr': ['서울', '서울']}
```

# **데이터 다루기**

## **데이터 읽기**

"dictionary 변수 명"["key 명"]을 통해서 value를 얻을 수 있다.

```py
mydict1 = {
    'Name': ['user1', 'user2'],
    'Age' : [20,15],
    'Addr' : ['서울','서울']
    }

print(mydict1['Name'])
print(mydict1['Age'][0])

출력 결과
['user1', 'user2']
20
```


## **데이터 추가**

"dictionary 변수 명"["key 명"]을 통해서 value를 추가할 수 있다.

```py
mydict1 = {
    'Name': ['user1', 'user2'],
    'Age' : [20,15],
    'Addr' : ['서울','서울']
    }

mydict1['Tel'] = ['1234','5678']
print(mydict1)

출력 결과
{'Name': ['user1', 'user2'], 'Age': [20, 15], 'Addr': ['서울', '서울'], 'Tel': ['1234', '5678']}
```


## **데이터 삭제**

del "dictionary 변수 명"["key 명"]을 통해서 key와 value를 삭제할 수 있다.

```py
mydict1 = {
    'Name': ['user1', 'user2'],
    'Age' : [20,15],
    'Addr' : ['서울','서울']
    }

del mydict1['Addr']
print(mydict1)

출력 결과
{'Name': ['user1', 'user2'], 'Age': [20, 15]}
```


## **데이터 변경**

"dictionary 변수 명"["key 명"]을 통해서 value를 변경할 수 있다.

```py
mydict1 = {
    'Name': ['user1', 'user2'],
    'Age' : [20,15],
    'Addr' : ['서울','서울']
    }

mydict1['Name'][0] = 'user3'
print(mydict1)

출력 결과
{'Name': ['user3', 'user2'], 'Age': [20, 15], 'Addr': ['서울', '서울']}
```

dictionary를 다른 dictionary를 통해 값을 변경 및 추가할 수 있다.

```py
sub_dict = {
    'Age' : [10, 18],
    'Tel' : ['1234','5678'],
    'ID' : ['hello','world'],
    }

mydict1.update(sub_dict)
print(mydict1)

출력 결과
{'Name': ['user1', 'user2'], 'Age': [10, 18], 'Addr': ['서울', '서울'], 'Tel': ['1234', '5678'], 'ID': ['hello', 'world']}
```


# **기타 속성**

여러 Attribute를 이용하여 데이터 값을 확인할 수 있다.

```py
mydict1 = {
    'Name': ['user1', 'user2'],
    'Age' : [20,15],
    'Addr' : ['서울','서울']
    }

print(mydict1.keys())   # mydict1의 key
print(mydict1.values()) # mydict1의 value
print(mydict1.items())  # mydict1의 key, value

for key, value in mydict1.items(): print('{:<10} : {}'.format(key, value))

출력 결과
dict_keys(['Name', 'Age', 'Addr'])
dict_values([['user1', 'user2'], [20, 15], ['서울', '서울']])
dict_items([('Name', ['user1', 'user2']), ('Age', [20, 15]), ('Addr', ['서울', '서울'])])
Name       : ['user1', 'user2']
Age        : [20, 15]
Addr       : ['서울', '서울']
```