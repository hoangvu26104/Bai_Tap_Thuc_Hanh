from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"Yêu cầu lấy tên của tất cả họa sĩ"

"Khoi tao Web"
driver = webdriver.Chrome()

"65-91 đại diện cho bảng chữ cái từ A-Z "
for i in range(65, 91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"

    try:

        driver.get(url)

        "Doi 1 chut de tai trang"
        time.sleep(5)

        "Lay ra tat ca the ul"
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")

        "Chon ul thu 2"
        ul_painters = ul_tags[20]

        "Lay ra tat ca the <li> thuoc ul_painters"
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        "Tao danh sach cac url"
        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
        titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tags]

        for title in titles:
            print(title)
    except:
        print("Error")

driver.quit()
