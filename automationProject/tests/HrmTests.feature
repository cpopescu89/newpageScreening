# Created by Chris at 08-Aug-22
Feature: VerifyLogin

  Scenario: Verify successful login
    Given I navigate to homepage
    When I log in with the credentials from the homepage
    Then the login is successful

  Scenario: Verify positions
    Given I navigate to homepage
    And I log in with the credentials from the homepage
    And the login is successful
    When I go to Recruitment
    And select Vacancies
    And I filter by "QA Lead"
    Then there is one position available for "Senior QA Lead"