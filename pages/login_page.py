from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators.locators import *

class LoginPage(Page):

	def __init__(self, context):
		Page.__init__(
			self,
			context)

	def input_chatter_name(self, name, browser):
		text_box = self.find_element(browser,
			*LoginPageLocators.WHO_R_U_TXT_BOX)
		text_box.send_keys(name)

	def input_chattee_name(self, name, browser):
		text_box = self.find_element(browser,
			*LoginPageLocators.WHO_U_TALK_T0_TXT_BOX)
		text_box.send_keys(name)

	def click_btn(self, btn_name, browser):
		page = LoginPageLocators
		btn_dict = {
				'Login': page.LOGIN_BTN
			} #dictionary of btns for scalability
		btn = self.find_element(browser,
			*btn_dict[btn_name])
		btn.click()

	def verify_not_in_page(self, page):
		if self.verify_page(page, self.browser[0]) == True:
			raise Exception("Bug! You should not be able to chat with yourself")
		else:
			pass


