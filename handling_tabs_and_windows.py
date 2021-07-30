import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("http://www.way2automation.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id=\"wrapper\"]/header/div[2]/div/div[2]/div/a[1]").click()

driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_xpath("//*[@id=\"user_email\"]").send_keys("checkstt@gmail.com")

time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
