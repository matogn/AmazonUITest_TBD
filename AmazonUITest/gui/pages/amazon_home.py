from selenium.webdriver.common.by import By

class AmazonHomePage:
    URL = 'https://amazon.com'
    SIGNIN_LINK = (By.XPATH,"//span[text()='Hello, Sign in']")

    def __init__(self,browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def click_signin_link(self):
        signin_link = self.browser.find_element_by_xpath(*self.SIGNIN_LINK)
        signin_link.click()