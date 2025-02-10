from behave import given, when, then, step
from API_Client import *
from Test_Data_Extractor import *
from Common import *
api_client = API_Client()
test_data = TestDataExtractor()


@given(u'List of users with given input array is created(create with list)')
def step_impl(context):
    context.config_users = test_data.get_users_test_data()
    payload = list()
    for row in context.table:
        payload.append(context.config_users[row["Users"]])
    context.response_full = api_client.send_request("POST", f"/user/createWithList", payload=payload)
    context.response = context.response_full.json()
    context.response_status_code = context.response_full.status_code

@given(u'List of users with given input array is created(create with array)')
def step_impl(context):
    context.config_users = test_data.get_users_test_data()
    payload = list()
    for row in context.table:
        payload.append(context.config_users[row["Users"]])
    context.response_full = api_client.send_request("POST", f"/user/createWithArray", payload=payload)
    context.response = context.response_full.json()
    context.response_status_code = context.response_full.status_code


@given(u'{user} is created')
def step_impl(context, user):
    context.response_full = api_client.send_request("POST", f"/user", payload=context.config_users[user])
    context.response = context.response_full.json()
    context.response_status_code = context.response_full.status_code

@then(u'User {user} details should be displayed')
def step_impl(context, user):
    for i in context.response:
        assert context.config_users[user][i]==context.response[i], f"{user} details not displayed"


@given(u'{user} is logged in')
def step_impl(context, user):
    username = context.config_users[user]["username"]
    password = context.config_users[user]["password"]
    context.response_full = api_client.send_request("GET", f"/user/login", params={"username": username, "password": password})
    context.response = context.response_full.json()
    context.response_status_code = context.response_full.status_code


@step(u'{user5} is updated with {user6} details')
def step_impl(context, user5, user6):
    username5 = context.config_users[user5]["username"]
    for i in context.config_users[user6]:
        context.response[i] = context.config_users[user6][i]
    context.response_full = api_client.send_request("PUT", f"/user/{username5}", payload=context.response)
    context.response = context.response_full.json()
    context.response_status_code = context.response_full.status_code




@then(u'User {user} details should not be displayed')
def step_impl(context, user):
        c=0
        for i in context.response:
            if context.response[i] != context.config_users[user][i]:
                c=0
                break
            else:
                c=1
        assert c==0, f"{user} details should not be present"


@step(u'User is logged out')
def step_impl(context):
    context.response_full = api_client.send_request("GET", f"/user/logout")
    context.response= context.response_full.json()
    context.response_status_code = context.response_full.status_code

@step('Get {user} details by username')
def step_impl(context, user):
    username = context.config_users[user]["username"]
    context.response_full = api_client.send_request("GET", f"/user/{username}")
    context.response= context.response_full.json()
    context.response_status_code = context.response_full.status_code

@step(u'{user} is deleted')
def step_impl(context, user):
    # user1 = context.config_users[user]
    username = context.config_users[user]["username"]
    context.response_full = api_client.send_request("DELETE", f"/user/{username}")
    context.response_status_code = context.response_full.status_code


@step("All the users from test data are deleted if present")
def step_imp(context):
    context.config_users = test_data.get_users_test_data()
    for i in context.config_users:
        if str(i).startswith("User"):
            step=f"When {i} is deleted"
            context.execute_steps(step)
