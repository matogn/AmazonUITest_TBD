from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class AmazonSigninPasswordPage:
    PASSWORD_INPUT = (By.ID, 'ap_password')

    @classmethod
    def __init__(self, browser):
        self.browser = browser

    def set_password(self, password):
        username_input = self.browser.find_element(*self.PASSWORD_INPUT)
        username_input.sendkeys(password + Keys.ENTER)
