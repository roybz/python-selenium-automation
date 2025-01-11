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
driver.get('https://www.amazon.com/sign-in')

# wait for 3 sec
sleep(3)

# click "need help?" url
needhelpanchor = driver.find_element(By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div[2]/div[1]/form/div/div/div/div[3]/div/a')
needhelpanchor.click()

# wait for 3 sec
sleep(3)

# click search button
forgotpasswordanchor = driver.find_element(By.XPATH, '//*[@id="auth-fpp-link-bottom"]')
forgotpasswordanchor.click()

# wait for 3 sec
sleep(3)

# verify  we're in the right place
passwordassistanceheader = driver.find_element(By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div/div/form/h1')
if passwordassistanceheader.text == 'Password assistance' : print('Test Passed')

driver.quit()
