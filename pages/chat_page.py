from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from login_page import LoginPage
from locators.locators import *
from config import Url
import unittest

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
		if len(self.chatter) == 2 and self._already_logged_in == False:
			#Login w/ Browser 1 
			login.input_chatter_name(self.chatter[0], self.browser[0])
			login.input_chattee_name(self.chatter[1], self.browser[0])
			login.click_btn('Login', self.browser[0])
			#Login w/ Browser 2
			login.input_chatter_name(self.chatter[1], self.browser[1])
			login.input_chattee_name(self.chatter[0], self.browser[1])
			login.click_btn('Login', self.browser[1])
			self._already_logged_in = True
		if len(self.chatter) == 3:
			login.input_chatter_name(self.chatter[2], self.browser[2])
			login.input_chattee_name(self.chatter[0], self.browser[2])
			login.click_btn('Login', self.browser[2])


