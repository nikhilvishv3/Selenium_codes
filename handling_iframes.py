import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
driver.maximize_window()

driver.switch_to.frame("iframeResult")
driver.find_element_by_xpath("/html/body/button").click()
    
driver.switch_to.default_content()
time.sleep(3)
frames = driver.find_elements_by_tag_name("iframe")

print("Total iframes: ",len(frames))

for frame in frames:
    print(frame.get_attribute("name"))
