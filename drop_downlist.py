from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome  import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time



driver =  webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver =  webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 10)


driver.get("https://www.wikipedia.com")
driver.maximize_window()

dropdown=driver.find_element_by_id("searchLanguage")
select = Select(dropdown)   
select.select_by_value("en")


options = driver.find_elements_by_tag_name("option")
for option in options:
    print("text is: ",option.text,"language is: ",option.get_attribute("lang"))

print("total dropdown values are: ",len(options))
