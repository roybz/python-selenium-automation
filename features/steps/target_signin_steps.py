from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when('Click sign in button from header')
def click_signin_from_header(context):
    context.driver.find_element(By.XPATH, '//*[@id="account-sign-in"]/span').click()
    sleep(3)

@when('Click on the signin button in the sidebar')
def click_sidebar_signin_button(context):
    context.driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/ul/div/button[1]').click()
    sleep(3)

@then('Verify sign in form opened')
def verify_we_are_in_right_place(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/h1/span').text
    assert expected_result in actual_result, f'Expected: {expected_result}, Actual: {actual_result}'