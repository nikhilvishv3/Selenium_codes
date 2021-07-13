from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome  import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver =  webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver =  webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 10)


driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[1]/div/label/input").send_keys("testautomation21")
driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[2]/div/label/input").send_keys("Think@12345")
driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[3]/button/div").click()
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div/div/button").click()
#Explicit wait
wait.until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/div/div/div[3]/button[2]"))).click()

# driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()  