import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver import ActionChains

"Khoi tao web"
driver = webdriver.Chrome()

"Mo trang web"
url = "https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=AfcR9il3Xj0_-HGhXE_VqU3wMnKp1bo8hHj6mBpF2OEKPtHVKrBqHzdbXWO_uTOIaburZZXEdGl2Rls4B4ZwAk-6CE63snE5rcrEYmCOCS7bvA&smuh=36123&lh=Ac_T8wg_HOmXorkeTSg"
driver.get(url)
time.sleep(5)

my_username = input("Nhap email hoac sdt: ")
my_password = getpass.getpass("Nhap password: ")

username_input = driver.find_element(By.XPATH, "//input[@name='email']")
password_input = driver.find_element(By.XPATH, "//input[@name='pass']")

time.sleep(3)

username_input.send_keys(my_username)
time.sleep(3)
password_input.send_keys(my_password + Keys.ENTER)


time.sleep(5)
# driver.quit()


url2 = "https://www.facebook.com/"
driver.get(url2)
time.sleep(10)

actionChains = ActionChains(driver)
post_label = driver.find_element(By.XPATH, """//span[contains(text(), "What's on your mind, Vu?")]""")
# post_label = driver.find_element(By.XPATH, "//div[@role='button']")

post_label.click()
# actionChains.send_keys('Vi du post').perform()

# actionChains.key_down(Keys.TAB).perform()
# actionChains.send_keys('Le Hoang Gia Vi' + Keys.ENTER).perform()

