from selenium import webdriver  # webdriver package
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager  # drivermanager package
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 使用.wdm指定driver位置
driver = webdriver.Chrome(ChromeDriverManager().install())  # 將webdriver設至變數driver

# driver = webdriver.Chrome(executable_path="C:\\browser_drivers\\chromedriver.exe")

driver.maximize_window()  # 最大化視窗
driver.get("https://www.google.com")  # 開啟指定url

#於搜尋欄輸入文字
search = driver.find_element_by_name("q")
search.clear()  # 清空輸入欄位
search.send_keys("")  # 輸入文字
search.send_keys(Keys.RETURN)  # enter

# 等待看板顯示後再開始取title
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
# )

#將標題放入titles
titles = driver.find_elements_by_class_name("LC201b")

# 寫出標題
for title in titles:
    print(title)

time.sleep(5)

# 點擊特定標籤
# link = driver.find_element_by_link_text("被征服的任性女友")
# link.click()
#
# driver.back()
# driver.back()
# driver.forward()

time.sleep(5)
driver.close()  # 關閉視窗


# print(driver.title)
# driver.get("http://www.google.com")
# print(driver.title)
# driver.back()
# print(driver.title)
# driver.forward()
# print(driver.title)