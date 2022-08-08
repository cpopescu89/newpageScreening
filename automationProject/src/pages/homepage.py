from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage


class HomePage(BasePage):
    _header_text_locator = "welcome"
    _recruitment_locator = "menu_recruitment_viewRecruitmentModule"
    _vacancies_locator = "menu_recruitment_viewJobVacancy"

    def get_header_text(self):
        return self.webdriver_utils.find_element_with_retry(By.ID, self._header_text_locator).text

    def recruitment_button(self):
        return self.webdriver_utils.find_element_with_retry(By.ID, self._recruitment_locator)

    def vacancies_button(self):
        return self.webdriver_utils.find_element_with_retry(By.ID, self._vacancies_locator)

    def mouse_over_recruitment(self):
        self.actions.move_to_element(self.recruitment_button()).perform()

    def click_vacancies(self):
        self.webdriver_utils.click_element_with_retry(self.vacancies_button())
