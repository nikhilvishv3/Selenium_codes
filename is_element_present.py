from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# def is_element_present(Id):
#     try:
#         driver.find_element_by_id(Id)
#         return True
#     except NoSuchElementException:
#         return False

def is_element_present(how, what):
    try:
        driver.find_element(by=how, value = what)
        return True
    except NoSuchElementException:
        return False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)

driver.get("https://www.gmail.com")
driver.maximize_window()

print(driver.find_element_by_id("identifierId").is_displayed())
# print(is_element_present("identifierId455"))
print(is_element_present(By.ID , "identifierId45"))
print(is_element_present(By.XPATH , "//*[@id=\"identifierId\"]"))


