# 이미지 크롤러 (Image Crawler)

이미지를 학습하는 AI를 개발할 경우, 데이터가 부족할 경우가 있다.

그 때 <b>구글 크롬</b>을 이용한 크롤러를 통해 데이터를 확보한다.

selenium를 이용하여 크롤러를 작성해보자.

* 공익에 이바지 하기위한 AI가 아닌 사적 이익을 추구하기 위한 무단 데이터 수집은 저작권 분쟁 여지가 있을 수 있으며, 현재까지도 AI 학습을 위한 데이터 복제 등에 대한 법이 개정되고 있으니 잘 알아보셔야 합니다.

```py
import os, time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scrollBrowserToEnd(driver):
    SCROLL_PAUSE_TIME = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try: driver.find_element_by_css_selector(".mye4qd").click()
            except: break
        last_height = new_height
    print(f"scroll End")

def crawlering_img(driver_path, googleSearchKeyword, saveImageDirectory):
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.set_window_size(1280, 1024)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
    googleSearchElement = driver.find_element_by_name("q")
    googleSearchElement.send_keys(googleSearchKeyword)
    googleSearchElement.send_keys(Keys.RETURN)
    scrollBrowserToEnd(driver)

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    for index, image in enumerate(images):
        index   = index+477
        try:
            image.click()
            time.sleep(2)
            imgURL = driver.find_element_by_xpath(
                "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{}]/a[1]/div[1]/img".format(
                    index + 1)).get_attribute("src")
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)

            if not (os.path.isdir(saveImageDirectory)): os.makedirs(saveImageDirectory)
            urllib.request.urlretrieve(imgURL, os.path.join(saveImageDirectory, googleSearchKeyword + '_{}.jpg'.format(index + 1)))
        except: pass
    print("Saved images : {}".format(index))
    driver.close()

googleSearchKeyword = "pikachu"
saveImageDirectory  = ".\\pikachu\\"
driver_path         = '.\\chromedriver.exe'
crawlering_img(driver_path, googleSearchKeyword, saveImageDirectory)
```