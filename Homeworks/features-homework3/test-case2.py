from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# wait for 3 sec
sleep(3)

# click "Sign in"
signinanchor = driver.find_element(By.CSS_SELECTOR, "a[data-test=\"@web/AccountLink\"]>span")
signinanchor.click()

# wait for 3 sec
sleep(3)

# click the other "Sign in"
signinbutton = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"accountNav-signIn\"]")
signinbutton.click()

# wait for 3 sec
sleep(3)

# verify we are in the right place
newestbutton = driver.find_element(By.CSS_SELECTOR, "button#login")
if newestbutton.text == 'Sign in with password' : print('Test Passed')

driver.quit()
