from behave import *
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(20)
@when('I open application')
def step_impl(context):
    context.driver.get(r'https://www.makemytrip.com/')
    context.driver.maximize_window()
    time.sleep(2)

@when('Click on offers button')
def step_impl(context):
    context.driver.find_element_by_xpath('//p[text()="Super Offers"]').click()

@when('click on Holidays button')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[text()='Holidays']").click()
    time.sleep(5)

@then('Click on selected offer in holidays')
def step_impl(context):
    context.driver.find_element_by_xpath("//p[text()='For Your European Summer Vacay:']").click()
    time.sleep(5)
    handles = context.driver.window_handles
    context.driver.switch_to.window(handles[1])
    time.sleep(5)

@then('click on book now button in offer')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[text()='BOOK NOW']").click()
    time.sleep(2)

@then('click on Next button')
def step_impl(context):
    context.driver.find_element_by_xpath("(//button['SKIP'])[2]").click()
    time.sleep(2)

@then('click on Next1 button')
def step_impl(context):
    context.driver.find_element_by_xpath("//button['SKIP']").click()
    time.sleep(1)

@then('click on cross mark')
def step_impl(context):
    context.driver.find_element_by_xpath('//span[@class="close closeIcon"]').click()
    time.sleep(3)
    handles = context.driver.window_handles
    context.driver.switch_to.window(handles[0])
    time.sleep(2)

@then('click on Trains button')
def step_impl(context):
    context.driver.find_element_by_xpath("(//span[text()='Trains'])[2]").click()
    time.sleep(3)

@then('Click on selected offer in Trains')
def step_impl(context):
    context.driver.find_element_by_xpath("//p[text()='Get Free Cancellation on Train Bookings!']").click()
    time.sleep(3)
#
# @then('click on book now button in trains offer')
# def step_impl(context):
#
#     text = context.driver.find_element_by_xpath('//a[@class="link"]').click()
#     time.sleep(2)
#     ac_obj = ActionChains(context.driver)
#     ac_obj.send_keys(Keys.PAGE_DOWN).perform()
#     context.driver.maximize_window()
#     time.sleep(3)
#     assert text == 'Book Now'
#     context.driver.close()
