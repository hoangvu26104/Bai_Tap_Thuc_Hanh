from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# Khoi tao web
driver = webdriver.Chrome()


"Mo trang"
url = "https://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

time.sleep(4)

"Lay ten hoa si"
try:
    name = driver.find_element(By.TAG_NAME, "h1").text
except:
    name = ""

try:
    birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
    birth = birth_element.text
    birth = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
except:
    birth = ""

try:
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
except:
    death = ""

try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
    nationality = nationality_element.text
except:
    nationality = ""


"Tao dictionary thong tin hoa si"

painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}
print(painter)
painter_df = pd.DataFrame([painter])


"Them thong tin va dataframe"
d = pd.concat([d, painter_df], ignore_index=True)
print(d)

driver.quit()


# "Tạo dataframe rỗng"
# d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})
#
# "Khoi tao webdriver"
# driver = webdriver.Chrome()
#
# " Mo trang"
# url = "https://en.wikipedia.org/wiki/Edvard_Munch"
# driver.get(url)
#
# "Doi 2 giay"
# time.sleep(2)
#
# "Lay ten hoa si"
# """Dùng try except là vì có thể 1 vài họa sĩ ko đủ dữ kiện để điền vào
# (Vd như k rõ ngày sinh, ngày mất và quốc tịch)"""
# try:
#     name = driver.find_element(By.TAG_NAME, "h1").text
# except:
#     name = ""
#
# "Lấy ngày sinh"
# try:
#     birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")

#     birth = birth_element.text
#     birth = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
# except:
#     birth = ""
#
# "Lấy ngày mất"
# try:
#     death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
#     death = death_element.text
#     death = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
# except:
#     death = ""
#
# "Lấy quốc tịch"
# try:
#     nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
#     nationality = nationality_element.text
# except:
#     nationality = ""
#
# "Tạo dictionary thông tin của họa sĩ"
# painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}
#
# "Chuyển đổi dictionary thành DataFrame"
# painter_df = pd.DataFrame([painter])
#
# "Thêm thông tin và DF"
# d = pd.concat([d, painter_df], ignore_index=True)
#
# "In DF"
# print(d)
#
# "Đóng web"
# driver.quit()