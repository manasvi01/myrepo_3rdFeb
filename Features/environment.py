import json

def before_scenario(context, scenario):
    print(f"Starting Regression scenario: {scenario.name}")
    context.response={}
    context.pet_payload = {
        "id": "id1",
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

def after_scenario(context, scenario):
    print(f"Finished Regression scenario: {scenario.name}")