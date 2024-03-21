from pip._internal.models import link
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

s = Service("C:/Users/Dell/OneDrive/Desktop/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get('http://google.com')
time.sleep(2)

user_input= driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys('onemg')

user_input.send_keys(keys.Enter)
time.sleep(1)

driver.find_element(by=By.XPATH, value='//*[@id="tads"]/div[1]/div/div/div/div[1]/a/div[1]/span')
link.click()