from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(2)

driver.get("https://jqueryui.com/resizable/")
driver.maximize_window()


driver.switch_to_frame(driver.find_element_by_xpath("//*[@id=\"content\"]/iframe"))
resizable =  driver.find_element_by_xpath("//*[@id=\"resizable\"]/div[3]")
ActionChains(driver).drag_and_drop_by_offset(resizable, 300,100).perform()
