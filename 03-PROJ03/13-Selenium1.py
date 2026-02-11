from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# define url
url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage 
driver.get(url)

# find the first name field 
first_name = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')
# fill out the first name field
first_name.send_keys("Fname")

# find the last name field 
last_name = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')
# find the last name field 
last_name.send_keys("Lname")

# find the email field 
email = driver.find_element(By.XPATH, '//*[@id="input-email"]')
# fill in the email field 
email.send_keys("something.email@email.com")

# find the telephone field 
telephone = driver.find_element(By.XPATH, '//*[@id="input-telephone"]')
# fill in the telephone field 
telephone.send_keys("1234567890")

# find the password field 
password = driver.find_element(By.XPATH, '//*[@id="input-password"]')
# fill in the password field 
password.send_keys("password")

# find the password confirm field 
password_confirm = driver.find_element(By.XPATH, '//*[@id="input-confirm"]')
# fill in the password confirm field 
password_confirm.send_keys("password")

# find the desired response to the newsletter subscribe field
newsletter_subscribe = driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/div[2]/label')
# click on it 
newsletter_subscribe.click()

# find the checkbox for agreeing to the terms 
agree = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/div/label')
# click on the agree checkbox
agree.click()

# find the continue button
continue_button = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input')
# click on the continue button
continue_button.click()

# scroll down by 200 units to view the lower part of the page
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause the program for 5 seconds to view the results
sleep(30)

# close the driver
driver.quit()