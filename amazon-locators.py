from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Amazon logo
driver.find_element(By.XPATH, '//*[@id="a-page"]/div[1]/div[1]/div/a/i')
# XPATH relative to an ID

# Create account header
driver.find_element(By.XPATH, '//*[@id="ap_register_form"]/div/div/h1')
# XPATH relative to an ID

# Name input
driver.find_element(By.ID, 'ap_customer_name')
# By ID

# Mobile or email input
driver.find_element(By.ID, 'ap_email')
# By ID

# Password input
driver.find_element(By.ID, 'ap_password')
# By ID

# Re-enter password input
driver.find_element(By.ID, 'ap_password_check')
# By ID

# Continue button
driver.find_element(By.ID, 'continue')
# By ID

# Conditions of use link
driver.find_element(By.XPATH, '//*[@id="legalTextRow"]/a[1]')
# By XPATH relative to an ID

# Privacy notice link
driver.find_element(By.XPATH, '//*[@id="legalTextRow"]/a[2]')
# By XPATH relative to an ID

# Sign in link
driver.find_element(By.XPATH, '//*[@id="ap_register_form"]/div/div/div[11]/a')
# By XPATH relative to an ID