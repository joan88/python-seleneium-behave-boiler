from config import Url
from pages.login_page import LoginPage
import time

@given('I am in the "{login_page}"')
def step_impl(context, login_page):
	page = LoginPage(context)
	page.open(Url.LOGIN_PAGE, page.browser[0])
	page.verify_page(login_page, page.browser[0])

@when('I input my name "{name}"')
def step_impl(context, name):
	page = LoginPage(context)
	page.input_chatter_name(name, page.browser[0])

@when('I input chattee\'s name "{name}"')
def step_impl(context, name):
	page = LoginPage(context)
	page.input_chattee_name(name, page.browser[0])

@when('I click "{button}"')
def step_impl(context, button):
	page = LoginPage(context)
	page.click_btn(button, page.browser[0])

@then('I should see the "{chat_page}"')
def step_impl(context, chat_page):
	page = LoginPage(context)
	page.verify_page(chat_page, page.browser[0])

