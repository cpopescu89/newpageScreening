from pytest_bdd import scenario, given, when, then, parsers


@scenario("HrmTests.feature", "Verify successful login")
def test_login_success():
    pass


@scenario("HrmTests.feature", "Verify positions")
def test_position_available():
    pass


@given("I navigate to homepage")
def step_impl(base_login_page):
    base_login_page.navigate_home()


@given("I log in with the credentials from the homepage")
@when("I log in with the credentials from the homepage")
def step_impl(base_login_page):
    page_credentials = base_login_page.get_credentials()
    base_login_page.login_with_credentials(page_credentials)


@given("the login is successful")
@then("the login is successful")
def step_impl(base_home_page):
    assert "Welcome" in base_home_page.get_header_text()


@when("I go to Recruitment")
def step_impl(base_home_page):
    base_home_page.mouse_over_recruitment()


@when("select Vacancies")
def step_impl(base_home_page):
    base_home_page.click_vacancies()


@when(parsers.cfparse('I filter by "{title}"'))
def step_impl(title, base_vacancies_page):
    base_vacancies_page.select_job_by_title(title)
    base_vacancies_page.click_search_button()


@then(parsers.cfparse('there is one position available for "{position}"'))
def step_impl(position, base_vacancies_page):
    assert base_vacancies_page.has_position(position)
