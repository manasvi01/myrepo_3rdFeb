@wipmanasvi
Feature: Regression Store
 Scenario: Searching, placing and deleting purchase orders and Getting pet inventory status
    Given Get Pet Inventories status
     Then Status Code should be 200
      And Response should be decoded and displayed

    Given Place following orders from test data
          | orders   |
          | Order1   |
          | Order2   |
          | Order3   |
     Then Status Code should be 200
#
    Given Find purchase Order1 by Order1 ID
     Then Order Order1 details should be displayed
      And Status Code should be 200

    Given Delete purchase Order2 by Order2 ID
     Then Status Code should be 200
     When Find purchase Order2 by Order2 ID
     Then Status Code should be 404