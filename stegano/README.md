# stegano

Steganography 모듈

stegano를 사용하기 위해서 pip3 install Stegano로 설치한다.

# **INDEX**

**1. [이미지에 글자 넣기](#이미지에-글자-넣기)**

**2. [이미지에 글자 추출](#이미지에-글자-추출)**


# **이미지에 글자 넣기**

이미지에 글자를 숨겨보자. PNG 밖에 안됐었다.

```py
import stegano
    
Steg_image = stegano.lsb.hide("bg.png", "Hello World")
Steg_image.save("Steg_image.png")
```


# **이미지에 글자 추출**

이미지에 숨겨진 글자를 추출해보자.

```py
import stegano
    
Hide_message = stegano.lsb.reveal("Steg_image.png")
print(Hide_message)
```