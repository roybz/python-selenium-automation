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

# click on the sign in button
signinbutton = driver.find_element(By.XPATH, '//*[@id="account-sign-in"]/span')
signinbutton.click()

# wait for 3 sec
sleep(3)

#click on the sidebar's sign in button
sidesideinbutton = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/ul/div/button[1]')
sidesideinbutton.click()

# wait for 3 sec
sleep(3)

# verify we're in the right place
messageanchor = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/h1/span')
if messageanchor.text == 'Sign into your Target account' : print('Test Passed')

driver.quit()