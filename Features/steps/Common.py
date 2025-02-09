from behave import step
@step("Status Code should be {code}")
def step_impl(context, code):
    print(context.response_status_code)
    assert str(code) == str(context.response_status_code), f"Status Code should be {code}"