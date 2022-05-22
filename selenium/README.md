# selenium

웹 브라우저의 상호 작용을 자동화하는 데 사용하는 패키지

# **INDEX**

**1. [Google 검색하기](#Google-검색하기)**

**2. [HTML 소스 보기](#HTML-소스-보기)**

**3. [스크린샷 찍기](#스크린샷-찍기)**

**4. [Chrome webdriver 설치](#Chrome-webdriver-설치)**

 - [Chrome 수동 설치](#Chrome-수동-설치)

 - [Chrome 자동 설치](#Chrome-자동-설치)

 - [webdriver 설치](#webdriver-설치)


# **Google 검색하기**

Google에 내가 원하는 단어를 검색해보자.

```py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip3 install webdriver_manager

url            = 'http://www.google.com'
driver_path    = '/root/chromedriver'
driver_options = Options()
driver_options.add_argument("--headless")
driver_options.add_argument("--no-sandbox")
driver          = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driver_options)

driver.get(url)
elem           = driver.find_element(by=By.NAME, value='q')
elem.send_keys('apple' + Keys.ENTER) # = Keys.RETURN
print(driver.title)

driver.get(url)
elem           = driver.find_element(by=By.NAME, value='q')
elem.send_keys('apple')
elem.submit()
print(driver.title)

driver.quit()
```

find_element로 다른 기준으로 찾을 경우 다음을 참고하자.

| by | description |
| :---: | :---: |
| By.ID | 태그의 id 값 |
| By.NAME | 태그의 name 값 |
| By.XPATH | 태그의 경로 값 |
| By.LINK_TEXT | 링크 텍스트 값 |
| By.PARTIAL_LINK_TEXT | 링크 텍스트의 자식 텍스트 값 |
| By.TAG_NAME | 태그 이름 값 |
| By.CLASS_NAME | 태그의 class 이름 값 |
| By.CSS_SELECTOR | css 선택자 값 |


# **HTML 소스 보기**

html의 소스를 얻을 수 있다.

```py
html = driver.page_source
print(html)
driver.quit()
```

# **스크린샷 찍기**

webdriver를 사용하면서 스크린샷을 찍을 수 있다.

한글로된 사이트의 경우 폰트가 없어 글씨가 깨질 수 있으므로 폰트를 설치해보자.

```sh
root@ubuntu:~# apt -y install fonts-nanum
```

별도로 윈도우 사이즈를 지정하지 않을 경우 전체 사이즈를 스크린샷을 찍지 못한다.

![](images/2022-05-23-00-55-49.png)

아래와 같이 전체 페이지로 사이즈를 정해서 스크린샷을 찍을 수 있다.

![](images/2022-05-23-00-56-46.png)

```py
url            = 'https://www.naver.com'
...
driver.save_screenshot('default_size.png')
total_height   = driver.execute_script("return document.body.parentNode.scrollHeight")
total_width    = driver.execute_script("return document.body.parentNode.scrollWidth")
driver.set_window_size(total_width, total_height)
driver.save_screenshot('full_size.png')
driver.quit()
```


# **Chrome webdriver 설치**

selenium의 webdriver를 자동으로 사용할 수 있지만, 인터넷환경이 안될 경우 webdriver를 설치 후 경로를 지정해줘야한다.

```py
service = ('/usr/bin/chromedriver')
webdriver.Chrome(service=service, options=driver_options)
```

## **Chrome 수동 설치**

[Chrome deb](https://www.slimjet.com/chrome/google-chrome-old-version.php)에 들어가서 deb를 다운받은 후

다음의 명령어로 설치한다.

```sh
root@ubuntu:~# dpkg -i google-chrome-stable_current_amd64.deb
```

버전이 맞는지 확인하자.

```sh
root@ubuntu:~# google-chrome --version
```

## **Chrome 자동 설치**

```sh
root@ubuntu:~# wget -q -O https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
root@ubuntu:~# echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
root@ubuntu:~# apt -y update
root@ubuntu:~# apt -y install google-chrome-stable
root@ubuntu:~# google-chrome --version
```

## **webdriver 설치**

Chrome 버전에 맞는 chrome driver를 다운받아야 한다.

[다음의 사이트](https://chromedriver.storage.googleapis.com/)에서 버전과 운영체제가 맞는 버전을 확인 후 URL뒤에 key값을 붙혀넣으면 된다.

다운 받은 후 실행권한을 주자.

실행권한을 주자.

```sh
root@ubuntu:~# chmod u+x chromedriver
```