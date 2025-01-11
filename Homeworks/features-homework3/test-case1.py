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

# click on the cart
cartanchor = driver.find_element(By.CSS_SELECTOR, "a[data-test=\"@web/CartLink\"]")
cartanchor.click()

# wait for 3 sec
sleep(3)

# verify right message is shown
messageanchor = driver.find_element(By.CSS_SELECTOR, "div[data-test=\"boxEmptyMsg\"]>h1")
if messageanchor.text == 'Your cart is empty' : print('Test Passed')

driver.quit()
