import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.BasePage import BasePage


class LoginPage(BasePage):
    _page_url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    _credentials_locator = "#content > div > span"
    _username_locator = "#txtUsername"
    _password_locator = "#txtPassword"
    _login_button_locator = "#btnLogin"

    def _get_credentials_string(self):
        return self.webdriver_utils.find_element_with_retry(By.CSS_SELECTOR, self._credentials_locator).text

    def username_field(self) -> WebElement:
        return self.webdriver_utils.find_element_with_retry(By.CSS_SELECTOR, self._username_locator)

    def password_field(self) -> WebElement:
        return self.webdriver_utils.find_element_with_retry(By.CSS_SELECTOR, self._password_locator)

    def login_button(self) -> WebElement:
        return self.webdriver_utils.find_element_with_retry(By.CSS_SELECTOR, self._login_button_locator)

    def navigate_home(self):
        self._driver.get(self._page_url)

    def get_credentials(self):
        credentials_string = self._get_credentials_string()
        user_regex = re.search("Username : (.*?) \|", credentials_string)
        pass_regex = re.search("Password : (.*?) \)", credentials_string)
        username = user_regex.group(1)
        password = pass_regex.group(1)
        return {"username": username, "password": password}

    def login_with_credentials(self, credentials):
        self.username_field().send_keys(credentials.get("username"))
        self.password_field().send_keys(credentials.get("password"))
        self.webdriver_utils.click_element_with_retry(self.login_button())
