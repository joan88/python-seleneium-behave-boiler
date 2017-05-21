from config import Url
from pages.chat_page import ChatPage
import time

@given('I am "{name}"')
def step_impl(context, name):
	page = ChatPage(context)
	page.check_if_message_received()
	if ChatPage.wins_are_open == False:
		page.open_win(3)
		ChatPage.wins_are_open = True
	if name not in ChatPage.chatter: 
		ChatPage.chatter.append(name)

@when('I send the message "{message}" to "{name}"')
def step_impl(context, name, message):
	page = ChatPage(context)
	if name not in ChatPage.chatter: 
		ChatPage.chatter.append(name)
	if message not in ChatPage.message:
		ChatPage.message.append(message)
	page.login_chatter(context)
	page.send_message()

@then('"{name}" should see the message "{message}"')
def step_impl(context, name, message):
	page = ChatPage(context)
	page.check_if_message_received()

@then('"{name}" should NOT see the message "{message}"')
def step_impl(context, name, message):
	page = ChatPage(context)
	page.check_if_message_received()



