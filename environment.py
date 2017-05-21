'''
@author Edgar Mamerto
@date 5/21/2017
'''
from selenium import webdriver

def before_all (context):
	
	# path = './chromedriver_mac'
	path = './chromedriver_win'

	# define Chrome browser instances
	context.browser = webdriver.Chrome(path)
	context.browser.set_window_position(0, 0)
	context.browser.set_window_size(750, 500)

	context.second_browser = webdriver.Chrome(path)
	context.second_browser.set_window_position(750, 0)
	context.second_browser.set_window_size(750, 500)

	context.third_browser = webdriver.Chrome(path)
	context.third_browser.set_window_position(0, 500)
	context.third_browser.set_window_size(750, 500)

def after_all(context):
	# close browsers after all have been executed
	browser = [
		context.browser, 
		context.second_browser, 
		context.third_browser
	]
	for i in range(len(browser)):
			browser[i].quit()
	