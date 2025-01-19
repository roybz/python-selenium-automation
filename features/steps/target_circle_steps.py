from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(3)

@then('Verify that there are at least 10 benefit cells')
def verify_benefit_cells(context):
    expected_benefit_cells_length = 10
    element_cells = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="@web/slingshot-components/CellsComponent/Link"]')
    assert len(element_cells) >= expected_benefit_cells_length, f'expected minimum {expected_benefit_cells_length} cells, got {len(element_cells)} cells'