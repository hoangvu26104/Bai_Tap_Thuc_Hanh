from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

"Lấy tất cả các tên của họa sĩ theo bảng chữ cái"

"Khoi tao Web"
driver = webdriver.Chrome()

"Mo trang"
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)
"""
    Thêm mới 
        Dòng dưới có tác dụng đợi các thành phần của web tải động
"""
WebDriverWait


"""Lay tat ca cac the <a> voi title chua 
'List_of_painters'"""
# tags_a = driver.find_elements(By.XPATH, "//a[contains(@title, 'List of painters')]")
tags_a = driver.find_elements(By.XPATH, "//a[starts-with(@title, 'List of painters')]")

"Tao ra danh sach lien ket"
links = [tag.get_attribute("href") for tag in tags_a]

"Tim hieu '/' (tim kiem tuyet doi trong xpath"
# link = []
# link.append(tags_a)

"Xuat thong tin"
for link in links:
    print(link)

# "Dong webdriver"
driver.quit()