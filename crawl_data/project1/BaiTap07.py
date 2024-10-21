from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re
from concurrent.futures import ThreadPoolExecutor

# Tạo một danh sách các trình duyệt (tab)
drivers = []

# Hàm khởi tạo và giữ lại 5 trình duyệt (hoặc tab)
def init_drivers(num_tabs=5):
    global drivers
    for _ in range(num_tabs):
        driver = webdriver.Chrome()
        drivers.append(driver)

# Hàm thu thập dữ liệu từ một liên kết họa sĩ, sử dụng trình duyệt đã được mở sẵn
def scrape_painter_data(link, driver):
    driver.get(link)
    time.sleep(1)  # Đợi trang tải
    
    # Biến lưu dữ liệu
    name = birth = death = nationality = ""
    
    # Thu thập tên
    try:
        name = driver.find_element(By.TAG_NAME, "h1").text
    except:
        pass
    
    # Thu thập ngày sinh
    try:
        birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
        birth = birth_element.text
        birth = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
    except:
        pass
    
    # Thu thập ngày mất
    try:
        death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
        death = death_element.text
        death = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
    except:
        pass
    
    # Thu thập quốc tịch
    try:
        nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
        nationality = nationality_element.text
    except:
        pass
    
    # Trả về dữ liệu dạng dict
    return {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

# Hàm xử lý truyền nhiều tham số vào hàm scrape_painter_data
def process_link(link_driver_tuple):
    link, driver = link_driver_tuple
    return scrape_painter_data(link, driver)

# Hàm chính để thu thập thông tin từ danh sách họa sĩ
def main():
    # Khởi tạo trình duyệt ban đầu để lấy danh sách liên kết
    driver = webdriver.Chrome()
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22M%22"
    driver.get(url)
    
    time.sleep(2)  # Đợi trang tải
    
    # Lấy danh sách các họa sĩ
    ul_tags = driver.find_elements(By.TAG_NAME, "ul")
    ul_painters = ul_tags[20]
    li_tags = ul_painters.find_elements(By.TAG_NAME, "li")
    
    # Lấy các liên kết
    links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
    driver.quit()

    # Khởi tạo 5 trình duyệt/tabs giữ nguyên
    init_drivers(5)

    # Tạo cặp (link, driver) để chuyển vào hàm process_link
    link_driver_pairs = [(links[i], drivers[i % 5]) for i in range(len(links))]

    # Sử dụng ThreadPoolExecutor với 5 luồng
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(process_link, link_driver_pairs))

    # Chuyển kết quả thành DataFrame
    df = pd.DataFrame(results)
    
    print(df)
    return df

# Chạy hàm chính
if __name__ == "__main__":
    df = main()
    df.to_excel("Painters1.xlsx", index=False)

    # Đóng tất cả trình duyệt sau khi hoàn thành
    for driver in drivers:
        driver.quit()