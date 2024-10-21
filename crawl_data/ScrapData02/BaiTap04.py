import getpass

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import getpass


# gecko_path = "E:\OSDS\osds\BTScrapDaTa02\geckodriver.exe"
gecko_path = "geckodriver.exe"
# Khởi tởi đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False


# Khởi tạo driver
driver = webdriver.Firefox(options=options, service=ser)

# Tạo url
url = 'https://www.reddit.com/login/'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(2)

my_email = input('Please provide your Email: ')
my_password = getpass.getpass('Please provide your password: ')

# "Dang nhap"
# username_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
# password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")
#
# # username_input = driver.find_element(By.XPATH, "//input[@name='username']")
# # password_input = driver.find_element(By.XPATH, "//input[@name='password']")
#
# time.sleep(3)
#
# username_input.send_keys(my_email)
# password_input.send_keys(my_password + Keys.ENTER)
# time.sleep(15)
#
# driver.quit()



# Đăng nhập
#username_input =driver.find_element(By.XPATH, "//input[@name='username']")
#password_input =driver.find_element(By.XPATH, "//input[@name='password']")

# Nhấn thông tin và nhấn nút Enter
#username_input.send_keys(my_email)
#password_input.send_keys(my_password + Keys.ENTER)
#time.sleep(5)
#button_login = driver.find_element(By.XPATH,"//button[text()='Log in']")
#button_login.click()



actionChains = ActionChains(driver)
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.send_keys(my_email).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys(my_password+Keys.ENTER).perform()

time.sleep(30)
# driver.quit()


# url2 = "https://www.reddit.com/submit?type=TEXT"
# driver.get(url2)
# time.sleep(2)
#
# textarea_input = driver.find_element(By.XPATH, "//textarea['@innerTextArea']")
#
# textarea_input.send_keys("Give some contents: ")
#
# actionChains.key_down(Keys.TAB).perform()
# actionChains.send_keys("Le Hoang Gia Vi")
#
#
# actionChains.key_down(Keys.TAB).perform()
# actionChains.send_keys("Muon viet gi cung duoc.")

# actionChains.key_down(Keys.TAB).perform()
# time.sleep(1)
# actionChains.key_down(Keys.TAB).perform()

# post_login = driver.find_element(Keys.ENTER).perform()



# Truy cap trang post bai
url2 = 'https://www.reddit.com/r/funny/submit/?type=TEXT'
driver.get(url2)
time.sleep(2)

for i in range(19):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

actionChains.send_keys('Vi du post').perform()

actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys('Le Hoang Gia Vi' + Keys.ENTER).perform()

for i in range(4):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

actionChains.key_down(Keys.Enter).perform()

time.sleep(15)
driver.quit()