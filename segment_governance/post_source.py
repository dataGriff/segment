import requests
import json
import os

url = "https://platform.segmentapis.com/v1beta/workspaces/googlemail-griff182uk/sources"

payload = json.dumps({
  "source": {
    "name": "workspaces/googlemail-griff182uk/sources/grifftest2",
    "catalog_name": "catalog/sources/javascript",
    "labels": {"environment":"dev"}
  }
})

bearer_token =  os.getenv('SEGMENT_TOKEN')
headers = {
  'Authorization': f'Bearer {bearer_token}',
  'Content-Type': 'application/json'
}


response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)