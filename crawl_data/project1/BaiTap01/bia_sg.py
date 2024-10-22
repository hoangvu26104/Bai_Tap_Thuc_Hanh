from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import sqlite3


# ##########################################################
# Ket noi den CSDL
conn = sqlite3.connect("Stock_Bia_SG.db")
# Tao doi tuong con tro 
c = conn.cursor()
try:
    c.execute("""
        Create Table Transacction(
            Id Integer Primary Key AutoIncrement,
            Day_Transaction Text,
            Open_price Integer,
            Highest_Price Integer,
            Lowest_Price Integer,
            Close_Price Integer,
            Change_Price Text,
            Change_Percent_Price Text,
            Volumn Integer
            )
    """)
except Exception as e:
    print(e)
# Ngat ket noi
conn.close()

# Tao ra 1 ham de them du lieu vao CSDL 
def them(Day_Transaction,
            Open_price,
            Highest_Price,
            Lowest_Price,
            Close_Price,
            Change_Price,
            Change_Percent_Price,
            Volumn):
    # Ket noi den CSDL
    conn = sqlite3.connect('Stock_Bia_SG.db')
    c = conn.cursor()

    c.execute("""
    Insert Into Transacction
        (
            Day_Transaction,
            Open_price,
            Highest_Price,
            Lowest_Price,
            Close_Price,
            Change_Price,
            Change_Percent_Price,
            Volumn
        )
    Values
        (
            :Day_Transaction,
            :Open_price,
            :Highest_Price,
            :Lowest_Price,
            :Close_Price,
            :Change_Price,
            :Change_Percent_Price,
            :Volumn
        )
    """, 
        {
            'Day_Transaction': day,
            'Open_price':open_price,
            'Highest_Price':highest_price,
            'Lowest_Price':lowest_price,
            'Close_Price':close_price,
            'Change_Price':change_price,
            'Change_Percent_Price':change_percent_price,
            'Volumn':volumn
        })
    # Chay lai du lieu khi da bi thay doi
    conn.commit()
    conn.close()
    



# ##########################################################
# # Tao 1 DataFrame rong
# d = pd.DataFrame({
#     'Day_Transaction':[],
#     'Open_Price':[],
#     'Highest_Price':[],
#     'Lowest_Price':[],
#     'Close_Price':[],
#     'Change_Price':[],
#     'Change_Percent_Price':[],
#     'Volumn':[]
#     })

# Khoi tao trang web 
driver = webdriver.Chrome()

# Mo trang web can lay du lieu
url = "https://simplize.vn/co-phieu/SAB/lich-su-gia"
driver.get(url)

time.sleep(5)

# Tim tat ca the table 
table_tags = driver.find_elements(By.TAG_NAME, "table")
# for index, value in enumerate(table_tags):
#     print(f"Index: {index}, Value: {value.text}")

# Tim tat ca the tr
tr_tags = table_tags[1].find_elements(By.TAG_NAME, "tr")
# for index, value in enumerate(tr_tags):
#      print(f"Index: {index}, Value: {value.text}")


td_tags = tr_tags[1].find_elements(By.TAG_NAME, "td")
# for index, value in enumerate(td_tags):
#     print(f"Index: {index} Value: {value.text}")


# Lay tat ca cac dong trong bang
rows = driver.find_elements(By.XPATH, "//tbody[@class='simplize-table-tbody']/tr[@class='simplize-table-row simplize-table-row-level-0']")
# for index, value in enumerate(rows):
#     print(f"Index: {index}, Value: {value.text}")
days = []
open_prices=[]
highest_prices=[]
lowest_prices=[]
close_prices=[]
change_prices=[]
change_percent_prices=[]
volumns=[]

try:
    for page_num in range(1, 3):
        page_xpath = f"//ul[@class='simplize-pagination css-10ewz0g']//li[contains(@class, 'simplize-pagination-item') and contains(@class, 'simplize-pagination-item-{page_num}')]/a"
        page = driver.find_element(By.XPATH, page_xpath)
        page.click()
        time.sleep(2)
        for row in rows: 
            # Lay ngay giao dich
            try:
                # day_element = row.find_element(By.XPATH, """//tbody[@class='simplize-table-tbody']
                                            #    /tr[@class='simplize-table-row simplize-table-row-level-0']/td[1]/h6""")
                day_element = row.find_element(By.XPATH, "./td[1]/h6")
                day = day_element.text
                days.append(day)
            except Exception as e:
                print(e)

            # Lay gia mo cua
            try:
                open_price_element = row.find_element(By.XPATH, "./td[2]/h6")
                open_price = open_price_element.text
                open_prices.append(open_price)
            except Exception as e:
                print(e)

            # Lay gia cao nhat
            try:
                highest_price_element = row.find_element(By.XPATH, "./td[3]/h6")
                highest_price = highest_price_element.text
                highest_prices.append(highest_price)
            except Exception as e:
                print(e)

            # Lay gia thap nhat
            try:
                lowest_price_element = row.find_element(By.XPATH, "./td[4]/h6")
                lowest_price = lowest_price_element.text
                lowest_prices.append(lowest_price)
            except Exception as e:
                print(e)

            # Lay gia dong cua
            try:
                close_price_element = row.find_element(By.XPATH, "./td[5]/h6")
                close_price = close_price_element.text
                close_prices.append(close_price)
            except Exception as e:
                print(e)

            # Lay thay doi gia
            try:
                change_price_element = row.find_element(By.XPATH, "./td[6]/h6")
                change_price = change_price_element.text
                change_prices.append(change_price)
            except Exception as e:
                print(e)

            # Lay % thay doi gia
            try:
                # change_percent_price_element = row.find_element(By.XPATH, "./td[7]/div/div/h6")
                change_percent_price_element = row.find_element(By.XPATH, "./td[7]//h6")
                change_percent_price = change_percent_price_element.text
                change_percent_prices.append(change_percent_price)
            except Exception as e:
                print(e)

            # Lay khoi luong
            try:
                volumn_element = row.find_element(By.XPATH, "./td[8]/h6")
                volumn = volumn_element.text
                volumns.append(volumn)
            except Exception as e:
                print(e)
            
            them(
                day,
                open_price,
                highest_price,
                lowest_price,
                close_price,
                change_price,
                change_percent_price,
                volumn
            )
            # # Tao Dictionary cho Bia_SG
            # Stock_Bia_SG = {
            #     'Day_Transaction': day,
            #     'Open_Price':open_price,
            #     'Highest_Price':highest_price,
            #     'Lowest_Price':lowest_price,
            #     'Close_Price':close_price,
            #     'Change_Price':change_price,
            #     'Change_Percent_Price':change_percent_price,
            #     'Volumn':volumn
            #     }

            # # Chuyen doi dictionary thanh DF
            # Stock_Bia_SG_df = pd.DataFrame([Stock_Bia_SG])

            # # Them thong tin vao DF chinh
            # d = pd.concat([d, Stock_Bia_SG_df], ignore_index=True)
            
            
except Exception as e:
    print(e)


# print("Ngay mo giao dich")
# print(days)
# print("##############################")

# print("Gia mo cua")
# print(open_prices)
# print("##############################")

# print("Gia cao nhat")
# print(highest_prices)
# print("##############################")

# print("Gia thap nhat")
# print(lowest_prices)
# print("##############################")

# print("Gia dong cua")
# print(close_prices)
# print("##############################")

# print("Thay doi gia")
# print(change_prices)
# print("##############################")

# print("% Thay doi gia")
# print(change_percent_prices)
# print("##############################")

# print("Khoi luong")
# print(volumns)
# print("##############################")


# print(d)

# # determining the name of the file
# file_name = 'Stock_Bia_SG.xlsx'

# # saving the excel
# d.to_excel(file_name)
# print('DataFrame is written to Excel File successfully.')
driver.quit()


