@wipmanasvi
Feature:Regression Pet store
  Scenario: Searching, Adding, updating and Deleting Pet data from store
    Given All pets from the test data are deleted if present
      And Add the following pets from test data
          | Pets   |
          | Pet1   |
          | Pet2   |
          | Pet3   |
          | Pet4   |
     Then Status Code should be 200
     When Get Pet Pet1 details by Pet1 ID
     Then Status Code should be 200
      And Pet Pet1 details should be displayed

    Given Get Pet Pet2 details by Pet2 ID
      And Update Pet2 ID with valid_id
     Then Status Code should be 200
     When Get Pet Pet2 details by valid_id
     Then Status Code should be 200
      And Updated Pet2 details should be displayed

    Given Get Pet Pet4 details by Pet4 ID
     Then Status Code should be 200
     When Update Pet4 ID with invalid_id
     Then Status Code should be 500
     When Get Pet Pet4 details by Pet4 ID
     Then Status Code should be 200
      And Pet4 ID should not get updated
     When Get Pet Pet4 details by invalid_id
     Then Status Code should be 404

    Given Get Pet Pet3 details by Pet3 ID
     Then Status Code should be 200
    Given Delete Pet3 by Pet3 ID
     Then Status Code should be 200
      And Get Pet Pet3 details by Pet3 ID
     Then Status Code should be 404
     Then Pet3 should get deleted

    Given Perform Form Update on Pet4 with name as "Bruno" and status as "Unavailable"
     Then Status Code should be 200
     When Get Pet Pet4 details by Pet4 ID
     Then Status Code should be 200
      And Pet4 details should be correct
#
    Given Find Pets by valid_status
     Then Status Code should be 200
      And All the Pet details with valid_status should be displayed
#
    Given Find Pets by invalid_status
    Then Status Code should be 200
     And Pet details with invalid_status should not be displayed

    Given Image is uploaded to Pet1
    Then Status Code should be 200








