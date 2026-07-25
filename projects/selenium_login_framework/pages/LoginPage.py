from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self,driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_username_field_visible(self):
        return self.is_visible(self.USER_NAME)

    def is_password_field_visible(self):
        return self.is_visible(self.PASSWORD)

    def is_login_button_visible(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def enter_username(self,username):
        self.do_send_keys(self.USER_NAME, username)


    def enter_password(self,password):
        self.do_send_keys(self.PASSWORD, password)


    def click_login(self):
        self.do_click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()





