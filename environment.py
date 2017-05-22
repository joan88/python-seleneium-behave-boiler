'''
@author Edgar Mamerto
@date 5/21/2017
'''
from selenium import webdriver

def before_all (context):
	
	path = './chromedriver'

	# define Chrome browser instances
	context.browser = webdriver.Chrome(path)
	context.browser.set_window_position(0, 0)
	context.browser.set_window_size(650, 750)

	context.second_browser = webdriver.Chrome(path)
	context.second_browser.set_window_position(450, 0)
	context.second_browser.set_window_size(650, 750)

	context.third_browser = webdriver.Chrome(path)
	context.third_browser.set_window_position(900, 0)
	context.third_browser.set_window_size(650, 750)

def after_all(context):
	# close browsers after all have been executed
	browser = [
		context.browser, 
		context.second_browser, 
		context.third_browser
	]
	for i in range(len(browser)):
			browser[i].quit()
	