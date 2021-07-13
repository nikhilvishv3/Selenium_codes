from selenium import webdriver
import time

# driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Users\\Administrator\\Downloads\\geckodriver-v0.29.1-win64\\geckodriver.exe")

driver.get("https://indpdm.vivo.com/rdms/explorer.jsp")
driver.maximize_window()

title = driver.title
print(title)

# assert "SeleniumHQ" in title -> this is used to check the particular string present in title

time.sleep(2)
# driver.quit() #it will close the current session
# driver.close() #it will close the whole session



