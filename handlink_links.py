from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome  import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time



driver =  webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 10)

driver.get("https://www.wikipedia.com")
driver.maximize_window()


print("------------handlink links------------")

links = driver.find_elements_by_tag_name("a")

print("Total links: ", len(links))
for link in links:
    print(" text is : ", link.text ,"link is: ",link.get_attribute("href"))

print("--------Links_in_block----------")

block = driver.find_element_by_xpath("//*[@id=\"www-wikipedia-org\"]/div[7]/div[3]")
block_link = block.find_elements_by_tag_name("a")

print("Total links: ", len(block_link))

for this in block_link:
    print("--link URL: ", this.get_attribute("href"))

print("------link_index-------")

print("ist link: ", block.find_elements_by_tag_name("a").__getitem__(2).get_attribute("href"))
