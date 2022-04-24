import json
import os
from os import listdir
from os.path import isfile, join
from pickle import FALSE
import sys
import requests
import re
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# ##need to be done per source...
# destinationsUrl = f"{baseUrl}/workspaces/{workspace}/sources/workshop_source/destinations"
# ##needs to be done per destination
# destinationsFilterUrl = f"{baseUrl}/workspaces/{workspace}/sources/workshop_source/destinations/azure-function/filters"

def get_json_file(file_name):
    """This function loads the given json available"""
    with open(file_name, 'r') as file:
        schema = json.load(file)
    return schema

def get_response(headers,url):
    """This function gets response"""
    url = url
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    payload = response.json()
    return payload

class SegmentConfig:
    def __init__(self, file_name):

        json_schema = get_json_file(file_name)

        self.name = json_schema['properties']['name']['value']
        self.tags = json_schema['properties']['tags']['items']['enum']
        self.environments = json_schema['properties']['environments']['items']['enum']
        self.products = json_schema['properties']['products']['items']['enum']
        self.sourceTypes = json_schema['properties']['sourceTypes']['items']['enum']
        self.destinationTypes = json_schema['properties']['destinationTypes']['items']['enum']

        baseUrl = "https://platform.segmentapis.com/v1beta"
        self.workspaceUrl = f"{baseUrl}/workspaces/{self.name}"
        self.rolesUrl = f"{baseUrl}/workspaces/{self.name}/roles"
        self.policiesUrl = f"{baseUrl}/workspaces/{self.name}/roles/-/policies"
        self.invitesUrl = f"{baseUrl}/workspaces/{self.name}/invites"
        self.sourcesUrl = f"{baseUrl}/workspaces/{self.name}/sources"

class SegmentSources:
    def __init__(self, payload):

        sources = (payload["sources"]) 
        self.sources = []
        for source in sources:
            self.sources.append(SegmentSource(source["display_name"],source["name"],source["labels"]))

    def  get_sources_test_result(self):
        results_html = "<h2>Sources Test Results</h2>"+"\n"
        for source in self.sources:
            result_html = source.get_source_test_result()
            results_html = results_html+result_html
        return results_html

class SegmentSource:
    def __init__(self, display_name, name, tags):

        self.display_name = display_name
        self.name = name
        self.tags = tags

    def get_source_details(self):
        print(f"Name: {self.name}, Display Name: {self.display_name}, Tags: {self.tags})")

    def get_source_test_displayname_result(self):
        test_result = re.search("(dev|uat|prd)_(griffco|dogadopt)_(blog|website|demo)", self.display_name)
        if(test_result is None):
            result_html = f"<p>Failure: Display name {self.display_name} does not meet naming standard.</p>"+"\n"
        else:
            result_html = f"<p>Success: Display name {self.display_name} does meet naming standard.</p>"+"\n"
        return result_html
   
    def get_source_test_name_result(self):
        test_result = re.search("workspaces/googlemail-griff182uk/sources/(dev|uat|prd)_(griffco|dogadopt)_(blog|website|demo)", self.name)
        if(test_result is None):
            result_html = f"<p>Failure: Name {self.name} does not meet naming standard.</p>"+"\n"
        else:
            result_html = f"<p>Success: Name {self.name} does meet naming standard.</p>"+"\n"
        return result_html

    def get_source_test_tags_result(self):
        result_html = "<h4>Source tags tests</h4>"+"\n"
        segment_config = SegmentConfig('schema/workspace.schema.json')
        tags_required = segment_config.tags
        for tag in tags_required:
            if(tag in self.tags):
                result_html = result_html+f"<p>Success: Source contains required tag '{tag}'.</p>"+"\n"
                tag_value = self.tags[tag]
                tag_values_allowed = segment_config.environments
                if(tag_value in tag_values_allowed):
                    result_html = result_html+f"<p>Success: Source contains allowed tag '{tag_value}' values for tag '{tag}'.</p>"+"\n"
                else:
                    result_html = result_html+f"<p>Failure: Source contains '{tag_value}' which is not allowed for tag '{tag}'.</p>"+"\n"
            else:
                result_html = result_html+f"<p>Failure: Source does not contain required tag '{tag}'.</p>"+"\n"
        return result_html

    def get_source_test_result(self):
        result_html = f"<h3>Source {self.display_name} Test Results</h3>"+"\n"
        result_html = result_html+self.get_source_test_displayname_result()
        result_html = result_html+self.get_source_test_name_result()
        result_html = result_html+self.get_source_test_tags_result()
        return result_html

# class SegmentDestinations:
#     def __init__(self, url):

#     sources_list = (source_payload["sources"])  

# class SegmentDestination:
#     def __init__(self, json):




