import pytest
from src.core import webdriverfactory
from src.pages.homepage import HomePage
from src.pages.loginpage import LoginPage
from src.pages.vacanciespage import VacanciesPage


@pytest.fixture(scope="function")
def init_driver(request):
    instance = webdriverfactory.WebDriverFactory()
    driver = instance.get_driver()

    yield driver

    instance.close_driver()
    print("TearDown done: close WebDriver")


@pytest.fixture()
def base_login_page(init_driver):
    return LoginPage(init_driver)


@pytest.fixture()
def base_home_page(init_driver):
    return HomePage(init_driver)


@pytest.fixture()
def base_vacancies_page(init_driver):
    return VacanciesPage(init_driver)
