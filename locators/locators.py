from selenium.webdriver.common.by import By

class LoginPageLocators(object):
  WHO_R_U_TXT_BOX = (By.XPATH, '//input[@placeholder="Who are you?"]')
  WHO_U_TALK_T0_TXT_BOX = (By.XPATH, '//input[@placeholder="Who are you talking to?"]')
  LOGIN_BTN = (By.XPATH, '//button[@type="submit" and contains(., "Login")]')

class ChatPageLocators(object):
  SAY_SOMETHING_TXT_BOX = (By.XPATH, '//input[@placeholder="Say something..."]')
  SEND_BTN = (By.XPATH, '//button[@type="submit" and contains(.,"Send")]')
  YELLOW_MSG = (By.XPATH, '//*[@id="chatBox" and contains(.,"Yellow")]')
  JELLO_MSG = (By.XPATH, '//*[@id="chatBox" and contains(.,"Jello")]')
  YOW_MSG = (By.XPATH, '//*[@id="chatBox" and contains(.,"Yow")]')

class CommonLocators(object):
  HEADING = (By.XPATH, '//*[@id="content"]/div/h1')






