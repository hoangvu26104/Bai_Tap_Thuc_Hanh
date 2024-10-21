import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


config = {
    'user': '100051207612370', 
    'password': 'hnv26104', 
    'delay_time': 10,
    'base_url': 'https://www.facebook.com/'
}


options = webdriver.ChromeOptions() 
options.headless = False
options.add_argument("--disable-notifications")
driver = uc.Chrome(options=options)
driver.maximize_window()

# hàm để cuộn trang
def scroll_down(pct=0.55, time_sleep=1):
    height = driver.execute_script("return document.body.scrollHeight")

    height = int(height*pct)
    for i in range(0, height, 300):
        driver.execute_script("window.scrollTo({}, {});".format(i, i+300))
        sleep(time_sleep)
        
driver.get(config["base_url"])
# WebDriverWait(driver, config['delay_time']).until(EC.presence_of_element_located((By.XPATH, '//button[@class="_66HDIC"]')))
# driver.save_screenshot("login.png")
# driver.find_element(By.XPATH, '//button[@class="_66HDIC"]').click()
# đợi trong 10s nếu tìm thấy XPATH thì tiếp tục
WebDriverWait(driver, config['delay_time']).until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))

# nhập tk và mk để login
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys(config['user'])
sleep(5)
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys(config['password'])
sleep(5)
driver.find_element(By.XPATH,'//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]').click()

# đợi 10s nếu url hiện tại sau dấu ? có chứa "is_from_login=true" thì tiếp tục
try:
    WebDriverWait(driver, config['delay_time']).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="fb_logo _8ilh img"]')))
    print("Login success")
except:
    print("Login failed")
sleep(1)
driver.save_screenshot("login.png")