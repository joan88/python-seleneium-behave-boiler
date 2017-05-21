from selenium import webdriver

def before_all (context):
	#define a Chrome browser instance
	context.browser = webdriver.Chrome('./chromedriver')
	context.second_browser = webdriver.Chrome('./chromedriver')
	context.third_browser = webdriver.Chrome('./chromedriver')

def after_all(context):
	browser = [context. browser, context.second_browser, context.third_browser]
	for i in range(len(browser)):
			browser[i].quit()
	