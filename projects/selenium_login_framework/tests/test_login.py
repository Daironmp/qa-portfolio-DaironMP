from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest
import pytest



@pytest.mark.usefixtures("setup")
class Test_Login(BaseTest):

    def test_login_page_title(self):
        login = LoginPage(self.driver)

        assert login.get_login_page_title(TestData.LOGIN_PAGE_TITLE) == TestData.LOGIN_PAGE_TITLE

    def test_username_field(self):
        login = LoginPage(self.driver)

        assert login.is_username_field_visible()

    def test_password_field(self):
        login = LoginPage(self.driver)

        assert login.is_password_field_visible()

    def test_login_button(self):
        login = LoginPage(self.driver)

        assert login.is_login_button_visible()

    def test_valid_login(self):
        login = LoginPage(self.driver)

        login.login(
            TestData.USER_NAME,
            TestData.PASSWORD
        )

        assert "inventory" in self.driver.current_url