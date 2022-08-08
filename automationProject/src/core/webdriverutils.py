from retrying import retry
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    WebDriverException
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverUtils:
    def __init__(self, driver):
        self._driver: WebDriver = driver

    max_retries = 5
    retry_wait = 1000
    explicit_wait_time = 5000

    @retry(
        stop_max_attempt_number=max_retries,
        wait_fixed=retry_wait
    )
    def find_element_with_retry(self, by_value, locator):
        elem = self._driver.find_element(by_value, locator)
        return elem

    @retry(
        stop_max_attempt_number=max_retries,
        wait_fixed=retry_wait
    )
    def click_element_with_retry(self, element):
        try:
            element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException, WebDriverException,
                NoSuchElementException) as ex:
            print(f"Failed to click element: {element.text} with error {type(ex)} ", )
            self._scroll_and_click_element(element)

    @retry(
        stop_max_attempt_number=max_retries,
        wait_fixed=retry_wait
    )
    def _scroll_and_click_element(self, element_to_click):
        self._driver.execute_script(
            """arguments[0].scrollIntoView({block: "center", inline: "nearest"})""",
            element_to_click,
        )
        element_to_click.click()

    def wait_for_text_to_be_present_in_element(self, element, text):
        return WebDriverWait(self._driver, self.explicit_wait_time).until(
            expected_conditions.text_to_be_present_in_element(locator=element, text_=text)
        )
