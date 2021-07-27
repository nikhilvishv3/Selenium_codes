from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# def is_element_present(how, what):
#     try:
#         driver.find_element(by=how, value = what)
#         return True
#     except NoSuchElementException:
#         return False

# i=1

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)

driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.maximize_window()

# driver.find_element_by_xpath("//div[4]/input[1]").click()
# driver.find_element_by_xpath("//div[4]/input[2]").click()
# driver.find_element_by_xpath("//div[4]/input[3]").click()    this is inefficient way 
# driver.find_element_by_xpath("//div[4]/input[4]").click()

# while is_element_present(By.XPATH, "//div[4]/input["+str(i)+"]"):        # it need a is_element_present function to operate
#     driver.find_element_by_xpath("//div[4]/input["+str(i)+"]").click()
#     i += 1

block = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]")
checkbox = block.find_elements(By.NAME , "sports")

for check in checkbox:
    check.click()
