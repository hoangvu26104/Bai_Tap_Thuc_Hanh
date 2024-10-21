from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
import time
import pandas as pd


# Đường dẫn đến file thực thi geckodriver
gecko_path = r"D:/Sele/project1/Exercise01/geckodriver.exe"

ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False


# Khởi tạo driver
driver = webdriver.Firefox(options = options, service=ser)

# Tạo url
url = 'https://pythonscraping.com/pages/files/form.html'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(1)

firstname_input = driver.find_element(By.XPATH, "//input[@name='firstname']")
lastname_input = driver.find_element(By.XPATH, "//input[@name='lastname']")

firstname_input.send_keys('Nguyen Vu')
time.sleep(3)
lastname_input.send_keys('Hoang')

time.sleep(2)
button = driver.find_element(By.XPATH, "//input[@type='submit']")
button.click()
time.sleep(5)
driver.quit()