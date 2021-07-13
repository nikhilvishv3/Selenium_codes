from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver =  webdriver.Chrome(executable_path=ChromeDriverManager().install())

# driver.get("https://indpdm.vivo.com/rdms/explorer.jsp")
driver.get("https://gmail.com")
driver.maximize_window()

# driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[1]/div[2]/form/p[1]/input").send_keys("95002530")
# driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[1]/div[2]/form/p[2]/input[2]").send_keys("Nikhil@201904")
# driver.find_element_by_xpath("//*[@id=\"login\"]").click()  

driver.find_element_by_xpath("//*[@id=\"identifierId\"]").send_keys("checkstt@gmail.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/div/button/span").click()
