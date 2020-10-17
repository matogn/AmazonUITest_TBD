from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class AmazonSigninUsernamePage:
    USERNAME_INPUT = (By.ID, 'ap_email')

    @classmethod
    def __init__(self, browser):
        self.browser = browser

    def set_username(self, username):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.sendkeys(username + Keys.ENTER)
