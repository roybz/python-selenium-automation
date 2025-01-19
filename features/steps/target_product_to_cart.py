from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

selected_product_price = 0.00

@given('We are on the Target home page')
def we_are_target_home(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when('Search for a {product_name}')
def search_for_product(context, product_name):
    search = context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
    search.clear()
    search.send_keys(product_name)

@when('Click on the search icon')
def click_on_search(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()
    sleep(3)

@when('Click on add to cart for the result in position {position}')
def click_on_add_to_cart(context, position):
    global selected_product_price
    selected_product_price = float(context.driver.find_element(By.XPATH, '//*[@id="pageBodyContainer"]/div/div[1]/div/div/div[4]/div/div/div[1]/div/div[1]/section/div/div['+str(int(position)+1)+']/div/div/div/div[2]/div/div/div[1]/div/div/span/span').text[1:])
    context.driver.find_element(By.XPATH, '//*[@id="pageBodyContainer"]/div/div[1]/div/div/div[4]/div/div/div[1]/div/div[1]/section/div/div['+str(int(position)+1)+']/div/div/div/div[3]/div[1]/div/button').click()
    sleep(3)

@when('Click on add to cart from the sidebar')
def click_on_add_to_cart_from_sidebar(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="shippingButton"]').click()
    sleep(3)

@when('Exit the sidebar')
def exit_the_sidebar(context):
    context.driver.find_element(By.XPATH, '/html/body/div[66]/div/div/div[1]/button[2]').click()
    sleep(3)

@when('Open the cart')
def open_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()
    sleep(3)

@then('Expect product to be added')
def expect_product_to_be_added(context):
    price_is_listed = False
    price_list = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="cartItem-price"]')
    if len(price_list) > 0:
        for price in price_list:
            if selected_product_price == float(price.get_attribute('innerHTML')[1:]) : price_is_listed = True
            break
    assert price_is_listed == True, f'Test failed'