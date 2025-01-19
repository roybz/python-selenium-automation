from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()
    sleep(3)

@then('Verify "Your cart is empty" message is shown')
def verify_your_cart_is_empty(context):
    expected_message = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, '//*[@id="cart-container"]/div[1]/div/div/div[2]/h1')
    assert expected_message == actual_result.text, f'{expected_message} != {actual_result.text}'