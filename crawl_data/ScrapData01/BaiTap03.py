from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""Yêu cầu lấy hết tên và đường link dẫn đến thông tin của họa sĩ 
trong trường hợp này là 'Những họa sĩ có chữ P'"""

"Khoi tao Web"
driver = webdriver.Chrome()

"Mo trang"
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22"
driver.get(url)

"Doi 1 chut de tai trang"
time.sleep(2)

"Lay ra tat ca the ul"
ul_tags = driver.find_elements(By.TAG_NAME, "ul")
print(ul_tags)
for index, value in enumerate(ul_tags):
    print(f"Index: {index}, Value: {value.text}")
"Chon ul thu 20"
ul_painters = ul_tags[20]

"Lay ra tat ca the <li> thuoc ul_painters"
li_tags = ul_tags[20].find_elements(By.TAG_NAME, "li")

"Tao danh sach cac url"
links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tags]

for link in links:
    print(link)
driver.quit()

for title in titles:
    print(title)
driver.quit()