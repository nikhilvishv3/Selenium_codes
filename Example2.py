from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver  = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

driver.get("https://indpdm.vivo.com/rdms/explorer.jsp")
driver.maximize_window()
title = driver.title
print("############\n The title is:",title)

time.sleep(2)
driver.quit()
driver.close()