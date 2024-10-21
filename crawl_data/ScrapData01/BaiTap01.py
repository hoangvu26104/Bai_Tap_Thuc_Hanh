from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"Yêu cầu là lấy tất cả các thẻ a có trong url"

"Khoi tao Web"
driver = webdriver.Chrome()

"Mo trang"
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)
time.sleep(2)

"Lay tat ca cac the <a>"
tags_a = driver.find_elements(By.TAG_NAME, "a")

"Tao ra danh sach lien ket"
links = [tag.get_attribute("href") for tag in tags_a]

"Xuat thong tin"
for link in links:
    print(link)

"Dong webdriver"
driver.quit()