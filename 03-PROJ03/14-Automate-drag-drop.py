from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://www.w3schools.com/html/html5_draganddrop.asp"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver.maximize_window()
driver.get(url)
source = driver.find_element(By.XPATH,'//*[@id="img1"]')
destination = driver.find_element(By.XPATH,'//*[@id="div2"]')
actions = ActionChains(driver)

actions.drag_and_drop(source,destination).perform()
sleep(5)
driver.quit()