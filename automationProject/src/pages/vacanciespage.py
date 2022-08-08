from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.pages.BasePage import BasePage


class VacanciesPage(BasePage):
    _job_title_dropdown_locator = "vacancySearch_jobTitle"
    _search_button_locator = "btnSrch"
    _table_column_selector = "//tr/td[count(//tr/th/a[contains(text(),'{}')]/../preceding-sibling::th)+1]"

    def select_job_by_title(self, title):
        select = Select(self.webdriver_utils.find_element_with_retry(By.ID, self._job_title_dropdown_locator))
        select.select_by_visible_text(title)

    def click_search_button(self):
        search_button = self.webdriver_utils.find_element_with_retry(By.ID, self._search_button_locator)
        self.webdriver_utils.click_element_with_retry(search_button)

    def has_position(self, position):
        # take only the Vacancy column, and do not search in all files
        vacancies_xpath_selector = self._table_column_selector.format("Vacancy")
        vacancies_column = self.webdriver_utils.find_element_with_retry(By.XPATH, vacancies_xpath_selector).text
        self.webdriver_utils.wait_for_text_to_be_present_in_element((By.XPATH, vacancies_xpath_selector), position)
        return position in vacancies_column
