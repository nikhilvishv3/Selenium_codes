from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(2)

driver.get("https://way2automation.com")
driver.maximize_window()

menu = driver.find_element_by_xpath("(//a[@href='javascript:void(0);'])[7]")
action = ActionChains(driver)
action.move_to_element(menu).perform()

driver.find_element_by_xpath("//*[@id=\"navbar-collapse-1\"]/ul/li[8]/ul/li[2]/a").click()



