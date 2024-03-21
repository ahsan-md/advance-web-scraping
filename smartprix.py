from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By


s= Service("C:/Users/Dell/OneDrive/Desktop/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.smartprix.com/mobiles')
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)


old_height= driver.execute_script('return document.body.scrollHeight')

while True:
    time.sleep(2)

    element = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div[3]/div[3]')
    driver.execute_script("arguments[0].scrollIntoView();", element)

    new_height=driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)

    if new_height == old_height:
        break
    old_height= new_height

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)