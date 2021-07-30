from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://deluxe-menu.com/popup-mode-sample.html")
driver.maximize_window()

img = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]/img")
ActionChains(driver).context_click(img).perform()
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id=\"dm2m1i1tdT\"]")).perform()
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id=\"dm2m2i1tdT\"]")).perform()
driver.find_element_by_xpath("//*[@id=\"dm2m3i1tdT\"]").click()