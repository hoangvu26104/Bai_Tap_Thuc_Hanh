from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re
# from selenium.webdriver.support.wait import WebDriverWait

######################################################
"I. Tạo noi chứa link và tạo DF rỗng"
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})
######################################################
# II. Lay ra tat ca duong dan de truy cap den painters
# Khởi tạo Webdriver
for i in range(65, 91):
    driver = webdriver.Chrome()
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22" + chr(i) + "%22"
    try:
        # Mở trang
        driver.get(url)

        # Đợi một chút để trang tải
        time.sleep(3)
        # WebDriverWait

        # Lay ra tat cac ca the ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        # print(len(ul_tags))

        # Chon the ul thu 21
        ul_painters = ul_tags[20]  # list start with index=0

        # Lay ra tat ca the <li> thuoc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        # Tao danh sach cac url
        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
        for x in links:
            all_links.append(x)
    except:
        print("Error!")

    # Dong webdrive
    driver.quit()

######################################################
# III. Lay thong tin cua tung hoa si

for link in all_links:
    print(link)

    try:
        # Khoi tao webdriver
        driver = webdriver.Chrome()
        # Mo trang
        url = link
        driver.get(url)

        # Doi 2 giay
        time.sleep(2)
        # WebDriverWait

        "Lấy tên họa sĩ"
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""
        "Lấy ngày sinh"
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
            # regex
        except:
            birth = ""
        "Lấy ngày mất"
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
        except:
            death = ""
        "Lấy quốc tịch"
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        "Tạo dict chứa thông tin của các họa sĩ"
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

        # CHuyen doi dictionary thanh DataFrame
        painter_df = pd.DataFrame([painter])

        "Thêm thông tin và DF chính"
        d = pd.concat([d, painter_df], ignore_index=True)

        # Dong web driver
        driver.quit()
    except:
        pass
####################
# IV. In thong tin
print(d)
# determining the name of the file
file_name = 'Painters.xlsx'

# saving the Excel
d.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')
