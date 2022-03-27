
import logging
import requests
import json
import base64
import datetime
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    key = 'A8k2YAUcLw6b3I4dbniDAcE8NO9HLIgJ:'
    key_bytes = key.encode('ascii')
    base_key = base64.b64encode(key_bytes)
    base_key_str = base_key.decode('ascii')
    print(base_key)
    print(f"Authorization: Basic {base_key_str}")

    dt = datetime.datetime.now()

    url = 'https://api.segment.io/v1/identify'
    body = {
    "userId": "019mr8mf4r",
    "traits": {
        "email": "pgibbons@example.com",
        "name": "Peter Gibbons",
        "industry": "Technology"
    },
    "context": {
        "ip": "24.5.68.47"
    },
    "timestamp": str(dt)
    }
    headers = {'content-type': 'application/json',  'Authorization': f'Basic {base_key_str}'}

    r = requests.post(url, data=json.dumps(body), headers=headers)

    if r.status_code==200:
        return func.HttpResponse(f"This HTTP triggered function executed successfully for identify.")

    url = 'https://api.segment.io/v1/track'
    body = {
    "userId": "019mr8mf4r",
    "event": "Item Purchased",
    "properties": {
        "name": "Leap to Conclusions Mat",
        "revenue": 14.99
    },
    "context": {
        "ip": "24.5.68.47"
    },
    "timestamp": str(dt)
    }
    headers = {'content-type': 'application/json',  'Authorization': f'Basic {base_key_str}'}

    r = requests.post(url, data=json.dumps(body), headers=headers)

    if r.status_code==200:
        return func.HttpResponse(f"This HTTP triggered function executed successfully for track.")
