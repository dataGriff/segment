from ast import Return
from logging import raiseExceptions
import requests
import json
import re

url = "https://platform.segmentapis.com/v1beta/workspaces/googlemail-griff182uk/sources"

payload={}
headers = {
  'Authorization': 'Bearer ...',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
payload = response.json()
dump = json.dumps(payload, indent=4)

sources_list = (payload["sources"])
team_names_list = ["griffteam"]

for source in sources_list:
  source_name = source["display_name"]

  test_result = re.search("(dev|uat|prd)_(griffco|dogadopt)_(blog|website|demo)", source_name)
  if(test_result is None):
    print(f"Fail: Source name {source_name} does not meet naming standard policy.")
    break
  else:
    print(f"Success: Source name {source_name} does meet naming standard policy.")

  try:
    environment_nc, brand_nc, source_nc = source_name.split("_")
  except Exception as e:
    print(f"Fail: Source name {source_name} does not meet naming standard policy.")

  try:
    environment_label = source["labels"]["environment"]
  except Exception as e:
    print(f"Fail: Source name {source_name} does not have an environment label.")
    break

  if(environment_label  == environment_nc):
    print(f"Success: Source name {source_name} environment {environment_label} is an expected environment label.")
  else:
    print(f"Fail: Source name {source_name} environment {environment_label} is not expected environment label.")

  try:
    team_label = source["labels"]["team"]
  except Exception as e:
    print(f"Fail: Source name {source_name} does not have a team label.")
    break

  if(team_label  in (team_names_list)):
    print(f"Success: Source name {source_name} team {team_label} is an expected team label.")
  else:
    print(f"Fail: Source name {source_name} team {team_label} is not expected team label.")

