from behave import *
from selenium import webdriver

@given("we have browser opened")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()

@when("we go to www.wp.pl")
def step_impl(context):
    context.browser.get("http://www.wp.pl")

@then("wp.pl site title starts with Wirtualna Polska")
def step_impl(context):
    print(context.browser.title.lower().startswith("Wirtualna Polska"))