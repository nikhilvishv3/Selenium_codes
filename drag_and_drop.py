from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)

# driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
# driver.maximize_window()

# draggable = driver.find_element_by_xpath("//*[@id=\"draggable\"]")
# droppable = driver.find_element_by_xpath("//*[@id=\"droppable\"]")

# ActionChains(driver).drag_and_drop(draggable, droppable).perform()

driver.get("http://way2automation.com/way2auto_jquery/droppable.php#load_box")
driver.maximize_window()
driver.switch_to_frame(driver.find_element_by_xpath("//*[@id=\"example-1-tab-1\"]/div/iframe"))
draggable = driver.find_element_by_xpath("//*[@id=\"draggable\"]")
droppable = driver.find_element_by_xpath("//*[@id=\"droppable\"]")
# ActionChains(driver).drag_and_drop(draggable, droppable).perform()
ActionChains(driver).drag_and_drop_by_offset(draggable, 39,230).perform()
