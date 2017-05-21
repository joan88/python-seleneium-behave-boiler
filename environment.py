'''
@author Edgar Mamerto
@date 5/21/2017
'''
from selenium import webdriver

def before_all (context):
	# define Chrome browser instances
	context.browser = webdriver.Chrome('./chromedriver')
	context.second_browser = webdriver.Chrome('./chromedriver')
	context.third_browser = webdriver.Chrome('./chromedriver')
	
def after_all(context):
	# close browsers after all have been executed
	browser = [
		context.browser, 
		context.second_browser, 
		context.third_browser
	]
	for i in range(len(browser)):
			browser[i].quit()
	