import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from login_page import LoginPage
from locators.locators import *
from config import Url


class ChatPage(Page):
	chatter = []
	message = []
	wins_are_open = False
	_already_logged_in = False

	def __init__(self, context):
		Page.__init__(
			self,
			context)

	'''
	This function allows you to open 
	number of windows dynamically
	'''	
	def open_win(self, num_of_wins):
		if num_of_wins > 3:
			raise Exception("Sorry! You have to extend your code to support more than 3 windows")
		else:	
			for i in range(0,num_of_wins): 
				self.open(Url.LOGIN_PAGE, self.browser[i])
				self.verify_page('Login Page', self.browser[i])

	def login_chatter(self, context):
		login = LoginPage(context)
		if len(self.chatter) == 2 and ChatPage._already_logged_in == False:
			#Login w/ Browser 1 
			login.input_chatter_name(self.chatter[0], self.browser[0])
			login.input_chattee_name(self.chatter[1], self.browser[0])
			login.click_btn('Login', self.browser[0])
			#Login w/ Browser 2
			login.input_chatter_name(self.chatter[1], self.browser[1])
			login.input_chattee_name(self.chatter[0], self.browser[1])
			login.click_btn('Login', self.browser[1])
			ChatPage._already_logged_in = True
		if len(self.chatter) == 3:
			login.input_chatter_name(self.chatter[0], self.browser[2])
			login.input_chattee_name(self.chatter[2], self.browser[2])
			login.click_btn('Login', self.browser[2])

	def send_message(self):
		#Scenario 1
		if len(self.message) == 1:
			text_box = self.find_element(self.browser[0],
				*ChatPageLocators.SAY_SOMETHING_TXT_BOX)
			send_btn = self.find_element(self.browser[0],
				*ChatPageLocators.SEND_BTN)
			text_box.send_keys(self.message[0])
			send_btn.click()
		#Scenario 2
		elif len(self.message) == 2:
			text_box = self.find_element(self.browser[1],
				*ChatPageLocators.SAY_SOMETHING_TXT_BOX)
			send_btn = self.find_element(self.browser[1],
				*ChatPageLocators.SEND_BTN)
			text_box.send_keys(self.message[1])
			send_btn.click()
		#Scenario 3
		elif len(self.message) == 3:
			text_box = self.find_element(self.browser[2],
				*ChatPageLocators.SAY_SOMETHING_TXT_BOX)
			send_btn = self.find_element(self.browser[2],
				*ChatPageLocators.SEND_BTN)
			text_box.send_keys(self.message[2])
			send_btn.click()
		else:
			raise Exception("Sorry! you have to extend the code to send more messages")
	def check_if_message_received(self):
		'''
		Check if user1 can read user2
		can read each other's messages
		'''
		try:
			if len(self.message) == 1:		
				self.find_element(self.browser[0],
				*ChatPageLocators.YELLOW_MSG)
			elif len(self.message) == 2:	
				self.find_element(self.browser[1],
				*ChatPageLocators.JELLO_MSG)
		except Exception as e:
			print ("Message may not have sent! ERROR: ", e)
		'''
		Check if user2 can read user3's messages from user1,
		if YES then raise an Error
		'''
		try:
			if len(self.message) == 3:	
				self.find_element(self.browser[2],
				*ChatPageLocators.YOW_MSG)
				raise Exception("ALERT! Message was sent to the wrong person!")
		except:
			pass






