# 코드 난독화 (Code Obfuscation)

python 내부 함수를 이용하여 코드 난독화하는 법을 알아본다.

subprocess를 이용한 예제를 통해 알아보자.

```py
import subprocess
p = subprocess.Popen(['whoami'], stdout=subprocess.PIPE, shell=True)
print(p.communicate)
```

해당 스크립트를 실행하면 cmd(Command Prompt, 명령 프롬프트)에서 whoami를 입력하였을 때의 결과와 똑같이 출력된다.

```
(b'desktop-dq3rcjm\\admin\r\n', None)
```

해당 스크립트를 난독화해보자.

첫번째로는 Module을 난독화하기 위한 문자열화한다.

<b>import subprocess</b>는 없애고 subprocess를 사용하는 곳은 <b>\_\_import\_\_('subprocess')</b>와 같이 바꾼다.

```py
p = __import__('subprocess').Popen(['whoami'], stdout=__import__('subprocess').PIPE, shell=True)
print(p.communicate())
```

해당 스크립트의 실행결과는 난독화 전 결과와 같다.

두번째로는 Attribute를 난독화하기 위한 문자열화한다.

<b>Popen</b>는 <b>getattr(\_\_import\_\_('subprocess'), 'Popen')</b>와 같이 바꾼다.

```py
p = getattr(__import__('subprocess'), 'Popen')(['whoami'], stdout=getattr(__import__('subprocess'), 'PIPE'), shell=True)
print(getattr(p, 'communicate')())
```

이제는 제일 짜증나는 문자열을 치환한다.

전략은 다음과 같이 "b"는 <b>True</b>의 클래스 이름은 <b>bool</b>인데 0번째 인덱스로 사용하는 것이다.

```py
print(True.__class__.__name__[0]) # b
```

Popen을 다음의 스크립트를 이용하여 바꾸어 보자.

```py
obfuscation_dict    = {
    'a':'().__class__.__eq__.__class__.__name__[2]',
    'b':'True.__class__.__name__[0]',
    'c':'().__class__.__eq__.__class__.__name__[11]',
    'd':'{}.__class__.__name__[0]',
    'e':'().__class__.__name__[-1]',
    'f':'vars.__class__.__name__[8]',
    'g':'True.__doc__[41]',
    'h':'vars.__class__.__name__[-3]',
    'i':'().__class__.__eq__.__class__.__name__[-5]',
    'j':'{}.__doc__[92]',
    'k':'{}.__doc__[104]',
    'l':'[].__class__.__name__[0]',
    'm':'vars.__class__.__name__[-6]',
    'n':'vars.__class__.__name__[6]',
    'o':'True.__class__.__name__[1]',
    'p':'str.__class__.__name__[2]',
    'q':'vars.__doc__[50]',
    'r':'().__class__.__eq__.__class__.__name__[-1]',
    's':'().__class__.__eq__.__class__.__name__[10]',
    't':'str.__class__.__name__[0]',
    'u':'().__class__.__name__[1]',
    'v':'{}.__doc__[109]',
    'w':'().__class__.__eq__.__class__.__name__[0]',
    'x':'True.__doc__[5]',
    'y':'str.__class__.__name__[1]',
    'z':'().__doc__[56]',
    '_':'abs.__class__.__name__[7]',
}

def Obfuscator(string):
    result = ''
    for s in string:
        if s.isupper(): s = 'getattr(' + Obfuscator(s.lower()) + ', ' + Obfuscator('upper') + ')()'
        try: result += (obfuscation_dict[s] + '+')
        except: result += (s + '+')
    return result[:-1]

print(Obfuscator('Popen'))
```

Popen의 난독화 결과는 다음과 같이 나오고

```
getattr(str.__class__.__name__[2], ().__class__.__name__[1]+str.__class__.__name__[2]+str.__class__.__name__[2]+().__class__.__name__[-1]+().__class__.__eq__.__class__.__name__[-1])()+True.__class__.__name__[1]+str.__class__.__name__[2]+().__class__.__name__[-1]+vars.__class__.__name__[6]
```

'Popen'에 결과값을 넣고 실행해도 결과는 같다.

```py
p = getattr(__import__('subprocess'), getattr(str.__class__.__name__[2], ().__class__.__name__[1]+str.__class__.__name__[2]+str.__class__.__name__[2]+().__class__.__name__[-1]+().__class__.__eq__.__class__.__name__[-1])()+True.__class__.__name__[1]+str.__class__.__name__[2]+().__class__.__name__[-1]+vars.__class__.__name__[6])(['whoami'], stdout=getattr(__import__('subprocess'), 'PIPE'), shell=True)
print(getattr(p, 'communicate')())
```

숫자도 난독화가 가능하다.

```py
# 1
print(
    (lambda _,__,___,____,_____:_)
    (*(lambda _,__,___: _(_,__,___))((lambda _,__,___:[__(___[(lambda: _).__code__.co_nlocals])]+_(_,__,___[(lambda _: _).__code__.co_nlocals:]) if ___ else []),lambda _: _.__code__.co_argcount,(lambda _:_,lambda _,__:_,lambda _,__,___:_,lambda _,__,___,____:_,lambda _,__,___,____,_____:_)))
)

# 2
print(
    (lambda _,__,___,____,_____:__) # : 이후 _개수가 출력되는 숫자이다.
    (*(lambda _,__,___: _(_,__,___))((lambda _,__,___:[__(___[(lambda: _).__code__.co_nlocals])]+_(_,__,___[(lambda _: _).__code__.co_nlocals:]) if ___ else []),lambda _: _.__code__.co_argcount,(lambda _:_,lambda _,__:_,lambda _,__,___:_,lambda _,__,___,____:_,lambda _,__,___,____,_____:_)))
)

# 9
print(
    (lambda _,__,___,____,_____:___*___) # : 이후 사칙연산에 의한 결과로 사용할 수 도 있다.
    (*(lambda _,__,___: _(_,__,___))((lambda _,__,___:[__(___[(lambda: _).__code__.co_nlocals])]+_(_,__,___[(lambda _: _).__code__.co_nlocals:]) if ___ else []),lambda _: _.__code__.co_argcount,(lambda _:_,lambda _,__:_,lambda _,__,___:_,lambda _,__,___,____:_,lambda _,__,___,____,_____:_)))
)
```

문자열과 숫자를 치환하면 한줄쓰기를 통해 더욱더 알아보기 힘들게 난독화한 후 base64로 인코딩을 통해 다시 난독화해보자.

```py
import base64
eval(compile(base64.b64decode('난독화한 코드를 base64로 인코딩 한 문자열'), '<string>', 'exec'))
```

문자열을 난독화 하는 또다른 방법이 있다.

```py
def Obfuscator(string):
    num = str(sum([ord(c) for c in string][i] * 256 ** i for i in range(len([ord(c) for c in string]))))
    result = '(lambda _,__:_(_,__))(lambda _,__: chr(__%256)+_(_,__//256) if __ else getattr((lambda: 0).__code__.co_lnotab,(lambda _,__,___,____,_____,______,_______,________,_________:{}.__class__.__name__[____-____]+().__class__.__name__[____-_____]+().__class__.__eq__.__class__.__name__[_________+__]+True.__class__.__name__[_]+{}.__class__.__name__[__-__]+().__class__.__name__[-_])(*(lambda _,__,___:_(_,__,___))((lambda _,__,___:[__(___[(lambda:_).__code__.co_nlocals])]+_(_,__,___[(lambda _:_).__code__.co_nlocals:]) if ___ else []),lambda _:_.__code__.co_argcount,(lambda _:_,lambda _,__:_,lambda _,__,___:_,lambda _,__,___,____:_,lambda _,__,___,____,_____:_,lambda _,__,___,____,_____,______:_,lambda _,__,___,____,_____,______,_______:_,lambda _,__,___,____,_____,______,_______,________:_,lambda _,__,___,____,_____,______,_______,________,_________:_))))(),' + num + ')'
    return result

print(Obfuscator('Popen'))
```