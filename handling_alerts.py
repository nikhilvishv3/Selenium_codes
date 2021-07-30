import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()

driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input[2]").click()
time.sleep(3)
Alert(driver).accept()

 