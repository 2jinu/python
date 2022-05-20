"""
def Obfuscator(string):
    num = str(sum([ord(c) for c in string][i] * 256 ** i for i in range(len([ord(c) for c in string]))))
    result = '(lambda _,__:_(_,__))(lambda _,__: chr(__%256)+_(_,__//256) if __ else getattr((lambda: 0).__code__.co_lnotab,(lambda _,__,___,____,_____,______,_______,________,_________:{}.__class__.__name__[____-____]+().__class__.__name__[____-_____]+().__class__.__eq__.__class__.__name__[_________+__]+True.__class__.__name__[_]+{}.__class__.__name__[__-__]+().__class__.__name__[-_])(*(lambda _,__,___:_(_,__,___))((lambda _,__,___:[__(___[(lambda:_).__code__.co_nlocals])]+_(_,__,___[(lambda _:_).__code__.co_nlocals:]) if ___ else []),lambda _:_.__code__.co_argcount,(lambda _:_,lambda _,__:_,lambda _,__,___:_,lambda _,__,___,____:_,lambda _,__,___,____,_____:_,lambda _,__,___,____,_____,______:_,lambda _,__,___,____,_____,______,_______:_,lambda _,__,___,____,_____,______,_______,________:_,lambda _,__,___,____,_____,______,_______,________,_________:_))))(),' + num + ')'
    return result

print(Obfuscator('Popen'))
"""