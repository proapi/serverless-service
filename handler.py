import json
from serverless_sdk import tag_event


def hello(event, context):
    tag_event('custom-tag', 'hello-world', {'custom': {'tag': 'data '}})

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }

    body = {
        "message": "This is just a test message as a response",
        "input": event
    }

    response = {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(body)
    }

    return response

