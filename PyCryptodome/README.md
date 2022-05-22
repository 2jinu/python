# PyCryptodome

암호화를 위한 Python 패키지

PyCryptodome를 사용하기 위해서 Linux의 경우 pip3 install pycryptodome로 설치하고 Windows의 경우 pip3 install pycryptodomex로 설치한다.

# **INDEX**

**1. [AES](#AES)**

**2. [DES](#DES)**

 - [b b](#b-b)


# **AES**

고급 암호화 표준(Advanced Encryption Standard)로서 대칭키를 사용하는 블럭 암호이다.

```py
from Cryptodome.Cipher import AES
import hashlib

class AESClass():
    def __init__(self, key, mode, iv=None):
        if not type(key) is bytes: key = hashlib.sha256(key.encode()).digest()
        if not type(iv) is bytes and iv: iv = iv.encode()[:AES.block_size]
        self._chiper = AES.new(key, mode, iv)
        
    def enc(self, data):
        if not type(data) is bytes: data = data.encode()
        while len(data) % AES.block_size != 0:
            data += (b'\x00' * (AES.block_size - len(data) % AES.block_size))
        return self._chiper.encrypt(data)
    
    def dec(self, data):
        if not type(data) is bytes: data = data.encode()
        return self._chiper.decrypt(data).decode()
    
key          = '12345678'
data         = 'this is plain text'
iv           = 'ABCDEFGHIJKLMNOP'
print('{}\t\t: {}'.format('원본', data))

aes_cbc      = AESClass(key, AES.MODE_CBC, iv)
enc_data_cbc = aes_cbc.enc(data)
aes_cbc      = AESClass(key, AES.MODE_CBC, iv)
dec_data_cbc = aes_cbc.dec(enc_data_cbc)

print('{}\t: {}'.format('암호화(CBC)', enc_data_cbc))
print('{}\t: {}'.format('복호화(CBC)', dec_data_cbc))
```


# **DES**

IBM에서 고안되어 NIST가 미국 표준 암호 알고리즘으로 채택된 대칭 암호화 알고리즘이다.

```py
from Cryptodome.Cipher import DES
        
class DESClass():
    def __init__(self, key, mode, iv=None):
        if not type(key) is bytes: key = key.encode()[:DES.key_size]
        if not type(iv) is bytes and iv: iv = iv.encode()[:DES.block_size]
        self._chiper = DES.new(key, mode) if mode == 1 or mode == 6 or mode == 9 else DES.new(key, mode, iv)
        """
        MODE_ECB     = 1
        MODE_CBC     = 2
        MODE_CFB     = 3
        MODE_OFB     = 5
        MODE_CTR     = 6
        MODE_OPENPGP = 7
        MODE_EAX     = 9
        """
        
    def enc(self, data):
        if not type(data) is bytes: data = data.encode()
        while len(data) % DES.block_size != 0:
            data += b'\x00'
        return self._chiper.encrypt(data)
    
    def dec(self, data):
        if not type(data) is bytes: data = data.encode()
        return self._chiper.decrypt(data).decode()
    
key          = '12345678'
data         = 'this is plain text'
iv           = 'ABCDEFGHIJKLMNOP'
print('{}\t\t: {}'.format('원본', data))

des_ecb      = DESClass(key, DES.MODE_ECB)
enc_data_ecb = des_ecb.enc(data)
des_ecb      = DESClass(key, DES.MODE_ECB)
dec_data_ecb = des_ecb.dec(enc_data_ecb)

print('{}\t: {}'.format('암호화(ECB)', enc_data_ecb))
print('{}\t: {}'.format('복호화(ECB)', dec_data_ecb))

des_ofb      = DESClass(key, DES.MODE_OFB, iv)
enc_data_ofb = des_ofb.enc(data)
des_ofb      = DESClass(key, DES.MODE_OFB, iv)
dec_data_ofb = des_ofb.dec(enc_data_ofb)

print('{}\t: {}'.format('암호화(OFB)', enc_data_ofb))
print('{}\t: {}'.format('복호화(OFB)', dec_data_ofb))

des_cbc      = DESClass(key, DES.MODE_CBC, iv)
enc_data_cbc = des_cbc.enc(data)
des_cbc      = DESClass(key, DES.MODE_CBC, iv)
dec_data_cbc = des_cbc.dec(enc_data_cbc)

print('{}\t: {}'.format('암호화(CBC)', enc_data_cbc))
print('{}\t: {}'.format('복호화(CBC)', dec_data_cbc))
```