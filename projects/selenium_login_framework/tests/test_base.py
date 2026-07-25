from config.config import TestData


class BaseTest:

    driver = None

    def setup_method(self):
        self.driver.get(TestData.BASE_URL)