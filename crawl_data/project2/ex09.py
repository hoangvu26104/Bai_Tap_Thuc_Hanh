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
# Đăng nhập
#username_input =driver.find_element(By.XPATH, "//input[@name='username']")
#password_input =driver.find_element(By.XPATH, "//input[@name='password']")

# Nhấn thông tin và nhấn nút Enter
#username_input.send_keys(my_email)
#password_input.send_keys(my_password + Keys.ENTER)
#time.sleep(5)

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
actionChains.send_keys(my_username).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys(my_password+Keys.ENTER).perform()
time.sleep(30)


# Truy cap trang post bai
url2 = 'https://www.reddit.com/user/Subject_Local_785/submit/?type=TEXT'
driver.get(url2)
time.sleep(10)

try:
        # Lấy tất cả các button trên trang
       buttons = driver.find_elements(By.TAG_NAME, "button")

       # Duyệt qua từng button
       for button in buttons:
           # Kiểm tra nếu nội dung của button chứa "Xem thêm" và "sản phẩm"
           if " Text " in button.text:
               # Di chuyển tới button và click
               button.click()
               break  # Thoát khỏi vòng lặp nếu đã click thành công
    
except Exception as e:
    print(f"Lỗi: {e}")


time.sleep(1)
    

actionChains.key_down(Keys.TAB).perform()
actionChains.key_down(Keys.TAB).perform()
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys('Vi du post').perform()
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys('Le Nhat Tung'+Keys.ENTER).perform()


time.sleep(15)
driver.quit()