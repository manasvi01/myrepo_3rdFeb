@wipmanasvi
Feature:User
 Scenario: Operations about user
    Given All the users from test data are deleted if present
    Given List of users with given input array is created(create with list)
          | Users |
          | User1 |
          | User2 |
     Then Status code should be 200

    Given List of users with given input array is created(create with array)
          | Users |
          | User3 |
          | User4 |
     Then Status code should be 200

    Given User5 is created
     Then Status Code should be 200
     When Get User5 details by username
     Then Status Code should be 200
      And User User5 details should be displayed

    Given User5 is logged in
     Then Status Code should be 200
    Given Get User5 details by username
     Then Status Code should be 200
     When User5 is updated with new details
     Then Status Code should be 200
     When Get User5 details by username
     Then Status Code should be 200
      And User User5 details should not be displayed
     When User is logged out
     Then Status Code should be 200

    Given User1 is logged in
     Then Status Code should be 200
     When Get User1 details by username
     Then Status Code should be 200
     When User1 is deleted
     Then Status Code should be 200
     When Get User1 details by username
     Then Status Code should be 404
