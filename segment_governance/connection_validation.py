from ast import Return
from logging import raiseExceptions
import requests
import json
import re
import os

workspace = "googlemail-griff182uk"
team_names_list = ["griffteam"]

baseUrl = "https://platform.segmentapis.com/v1beta"
sourcesUrl = f"{baseUrl}/workspaces/{workspace}/sources"

source_payload={}
bearer_token =  os.getenv('SEGMENT_TOKEN')
headers = {
  'Authorization': f'Bearer {bearer_token}',
  'Content-Type': 'application/json'
}

source_response = requests.request("GET", sourcesUrl, headers=headers, data=source_payload)
source_payload = source_response.json()
##dump = json.dumps(payload, indent=4) ##for debugging

sources_list = (source_payload["sources"])

for source in sources_list:
  source_display_name = source["display_name"]
  source_name = source["name"]
  destinationsUrl = f"{baseUrl}/{source_name}/destinations"
  destinations_response = requests.request("GET", destinationsUrl, headers=headers)
  destinations_list = destinations_response.json()

  test_result = re.search("(dev|uat|prd)_(griffco|dogadopt)_(blog|website|demo)", source_display_name)
  if(test_result is None):
    print(f"Fail: Source name {source_display_name} does not meet naming standard policy.")
    break
  else:
    print(f"Success: Source name {source_display_name} does meet naming standard policy.")

  try:
    environment_nc, brand_nc, source_nc = source_display_name.split("_")
  except Exception as e:
    print(f"Fail: Source name {source_display_name} does not meet naming standard policy.")

  try:
    environment_label = source["labels"]["environment"]
  except Exception as e:
    print(f"Fail: Source name {source_display_name} does not have an environment label.")
    break

  if(environment_label  == environment_nc):
    print(f"Success: Source name {source_display_name} environment {environment_label} is an expected environment label.")
  else:
    print(f"Fail: Source name {source_display_name} environment {environment_label} is not expected environment label.")

  try:
    team_label = source["labels"]["team"]
  except Exception as e:
    print(f"Fail: Source name {source_display_name} does not have a team label.")
    break

  if(team_label  in (team_names_list)):
    print(f"Success: Source name {source_display_name} team {team_label} is an expected team label.")
  else:
    print(f"Fail: Source name {source_display_name} team {team_label} is not expected team label.")

