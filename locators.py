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

# Email field
driver.find_element(By.ID, "ap_email")
# By  ID

# Continue button
driver.find_element(By.ID, "continue")
# By ID

# Conditions of use link
driver.find_element(By.XPATH, "//*[@id='a-page']/div[1]/div[4]/div[2]/ul/li[1]/a")
# XPATH relative to ID

# Privacy Notice link
driver.find_element(By.XPATH, "//*[@id='a-page']/div[1]/div[4]/div[2]/ul/li[2]/a")
# XPATH relative to ID

# Need help link
driver.find_element(By.XPATH, "//*[@id='authportal-main-section']/div[2]/div[2]/div[1]/form/div/div/div/div[3]/div/a")
# XPATH relative to ID

# Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")
# By ID

# Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")
# By ID

# Create your Amazon account button
driver.find_element(By.ID, "ap-other-signin-issues-link")
# By ID