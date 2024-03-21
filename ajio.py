from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:/Users/Dell/OneDrive/Desktop/chromedriver.exe")
driver=webdriver.Chrome(service= s)
driver.get('https://www.ajio.com/men-backpacks/c/830201001')
old_height= driver.execute_script('return document.body.scrollHeight')
while True:
    new_height=driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)

    if new_height == old_height:
        break
    old_height= new_height

html = driver.page_source

with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)