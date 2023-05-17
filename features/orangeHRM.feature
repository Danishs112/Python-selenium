Feature: OrangeHRM

  Scenario: Logo presence on ORANGEHRM homepage
    Given launch chrome driver
    When open orange hrm homepage
    And verify that logo is present on the homepage
    And I fill "search doctors" on the search input field
#    Then close browser