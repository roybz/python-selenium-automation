from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target home page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when('Populate search script with {search_string}')
def populate_search(context, search_string):
    search = context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
    search.clear()
    search.send_keys(search_string)

@when('Click on target search icon')
def click_search(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()
    sleep(3)

@then('Product results for {search_string} are displayed')
def product_results_displayed(context, search_string):
    expected_results = search_string
    actual_results = context.driver.find_element(By.XPATH, '//*[@id="pageBodyContainer"]/div/div[1]/div/div/div[4]/div/div/div[3]/div/div/span')
    assert expected_results in actual_results.text, f'Test failed'