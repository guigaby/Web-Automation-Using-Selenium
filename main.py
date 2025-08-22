from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

chrome_options = Options()
chrome_options.add_argument('--disable-notifications')

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com/")
time.sleep(5)

driver.get("https://www.instagram.com/")
time.sleep(3)



elemento = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input")
elemento.send_keys("test.lg@gmail.com0")
senhaaaa = driver.find_element(By.NAME, "password")
senhaaaa.send_keys("123456789")
senhaaaa.send_keys(Keys.RETURN)
time.sleep(5)
time.sleep(30)

