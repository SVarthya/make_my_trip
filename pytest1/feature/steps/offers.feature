Feature:Offers
  Background: common steps
    Given I launch chrome browser
    When I open application
    And Click on offers button

  Scenario: Holidays offer
    And  click on Holidays button
    Then Click on selected offer in holidays
    Then click on book now button in offer
    Then click on Next button
    Then click on Next1 button
    Then click on cross mark
    Then click on Trains button
    Then Click on selected offer in Trains
#    Then click on book now button in trains offer
