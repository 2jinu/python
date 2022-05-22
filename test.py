from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
