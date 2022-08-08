from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

from src.core.webdriverutils import WebDriverUtils


class BasePage():
    def __init__(self, driver):
        self._driver: WebDriver = driver
        self.webdriver_utils = WebDriverUtils(self._driver)
        self.actions = ActionChains(self._driver)
