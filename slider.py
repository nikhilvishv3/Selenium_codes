from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(2)

driver.get("https://flipkart.com")
driver.maximize_window()

driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_xpath("//*[@id=\"container\"]/div/div[3]/div[3]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/a/div[1]/div/img").click()
element = driver.find_element_by_xpath("//*[@id=\"container\"]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[3]/div[1]/div[4]")


size = element.size
location = element.location
h,w = size['height'], size['width']

print(size)
print(location)


slider = driver.find_element_by_xpath("//*[@id=\"container\"]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[3]/div[1]/div[2]/div")

action = ActionChains(driver)
action.drag_and_drop_by_offset(slider,-w/2,0).perform()


