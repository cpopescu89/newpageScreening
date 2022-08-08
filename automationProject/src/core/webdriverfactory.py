from selenium import webdriver
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class WebDriverFactory():

    def __init__(self):
        self.__desired_capabilities = DesiredCapabilities.CHROME
        self.web_driver = None
        self.driver_initialized = False
        self.__chrome_options = Options()

    @property
    def driver_initialized(self):
        return self._driver_initialized

    @driver_initialized.setter
    def driver_initialized(self, initialized_state):
        self._driver_initialized = initialized_state

    def get_driver(self):
        if not self.driver_initialized:
            self._start_maximized()
            self._create_webdriver_instance()
            print("Selenium initialized with ChromeDriver")
            self.driver_initialized = True
        return self.web_driver

    def _create_webdriver_instance(self):
        try:
            self.web_driver = webdriver.Chrome(
                options=self.__chrome_options,
                desired_capabilities=self.__desired_capabilities
            )
        # when the ChromeDriverStrategy executable does not match with the installed Chrome/Chromium version,
        # SessionNotCreated error is raised
        except SessionNotCreatedException as e:
            print(e.msg)
            raise
        # WebDriverException is raised if the executable is not found in the PATH env var
        except WebDriverException as e:
            print(e)
            print(e.msg)
            raise

    def _start_maximized(self):
        self.__chrome_options.add_argument("--start-maximized")

    def close_driver(self):
        print("Closing WebDriver")
        if self.web_driver:
            self.web_driver.quit()
        else:
            print("WebDriver is None, web_driver.quit() skipped")
        self.driver_initialized = False
