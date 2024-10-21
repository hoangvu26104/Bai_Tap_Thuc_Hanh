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
import getpass


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
url = 'https://www.reddit.com/login/'

driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(3)

# button_login = driver.find_element(By.XPATH, '//button[contains(@class, "px-sm") and contains(@class, "hover:no-underline") and contains(@class, "button-medium") and contains(@class, "px-[var(--rem14)]") and contains(@class, "button-brand") and contains(@class, "items-center") and contains(@class, "justify-center") and contains(@class, "inline-flex")]')
# button_login.click()

my_username = input('Please provide your email:')
my_password = getpass.getpass('Please provide your password:')

username_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")
time.sleep(3)

username_input.send_keys(my_username)
password_input.send_keys(my_password+Keys.ENTER)

time.sleep(1000)

# button = driver.find_element(By.XPATH,'//button[@class="login w-100 button-large px-[var(--rem14)] button-brand items-center justify-center button inline-flex"]').click()

driver.quit()
