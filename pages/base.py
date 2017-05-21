from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locators import *
import unittest
import time

class Page(unittest.TestCase):
    def __init__(self, context):
        self.browser = [
            context.browser,
            context.second_browser,
            context.third_browser,
        ]
 
    def find_element(self,browser, *locator):
        browser.implicitly_wait(30)
        time.sleep(3)
        return browser.find_element(*locator)

    def open(self,url,browser):
        browser.get(url)

    def verify_page(self,page,browser):
        if page == "Login Page":
            heading_text = browser.find_element(*CommonLocators.HEADING).text
            self.assertEqual("Sign in to Chat", heading_text) 
        elif page == "Chat Page":
            heading_text = browser.find_element(*CommonLocators.HEADING).text
            self.assertEqual("Chatting", heading_text) 
        else:
            raise Exception(page + ' Does Not Exist!')

        



