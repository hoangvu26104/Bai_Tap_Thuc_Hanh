from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Khởi tạo web driver
driver = webdriver.Chrome()

# Mở trang web
url = 'https://gochek.vn/collections/all'
driver.get(url)
# Đợi trang tải
time.sleep(4)

# Cuộn xuống để trang được tải hết nội dung
body = driver.find_element(By.TAG_NAME, "body")
for _ in range(50):
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.2)

# Tìm tất cả các thẻ div chứa thông tin sản phẩm
divs = driver.find_elements(By.XPATH, "//div[@class='col-md-3 col-sm-4 col-xs-6 pro-loop col_fix20']")

discount_percent_prices = []
product_pictures = []
names_product = []
prices = []

# Lấy dữ liệu từ các thẻ div
for div in divs:
    # Tìm khuyến mãi của sản phẩm
    try:
        discount_percent_price_element = div.find_element(By.XPATH, ".//div[@class='product-sale']//span").text
        discount_percent_prices.append(discount_percent_price_element)
    except Exception as e:
        discount_percent_prices.append("N/A")  # Nếu không có, thêm giá trị "N/A"
        print(f"Lỗi: {e}")

    # Tìm hình ảnh sản phẩm
    try:
        product_picture_element = div.find_element(By.CSS_SELECTOR, "div.product-img img").get_attribute('src')
        product_pictures.append(product_picture_element)
    except Exception as e:
        print(f"Lỗi: {e}")

    # Tìm tên sản phẩm
    try:
        name_product_element = div.find_element(By.XPATH, ".//div[@class='product-detail clearfix']//h3").text
        names_product.append(name_product_element)
    except Exception as e:
        print(f"Lỗi: {e}")

    # Tìm giá sản phẩm
    try:
        price_element = div.find_element(By.XPATH, ".//div[@class='box-pro-detail']//del").text
        prices.append(price_element)
    except Exception as e:
        print(f"Lỗi: {e}")

# Tạo DataFrame để lưu dữ liệu
df = pd.DataFrame({
    "Khuyến Mãi": discount_percent_prices,
    "Hình Ảnh": product_pictures,
    "Tên Sản Phẩm": names_product,
    "Giá Sản Phẩm": prices
})
# In ra DataFrame
print(df)
try:
    # Lưu dữ liệu vào file Excel
    df.to_excel("San_Pham.xlsx", index=False)
except Exception as e:
    print(e)