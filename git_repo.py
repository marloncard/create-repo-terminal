#!/usr/bin/env python3
"""
Create GITHUB Repository
"""
import requests
import json
import pathlib


with open('{home}/.credentials/GITHUB.txt'.format(home=pathlib.Path.home())) as cred:
    TOKEN = cred.read().strip()

BASE_URL = "https://api.github.com"
ENDPOINT = "/user/repos"
PAYLOAD = {}

# Create dictionary items at input
repo_name = PAYLOAD["name"]=input("Name of repo: ")
repo_description = PAYLOAD["description"]=input("Description of repo: ")

private = input("Private repo (true/false)? ") 
while True:
    if private.lower() == "true":
        PAYLOAD["private"] = True
        break
    elif private.lower() == "false":
        PAYLOAD["private"] = False
        break
    else:
        private = input("Private repo (true/false): ")


def create_repo():
    """
    Github API call to create repository, using github api v3
    """
    url = BASE_URL + ENDPOINT
    auth = ("marloncard", TOKEN)
    r = requests.post(url, auth=auth, data=json.dumps(PAYLOAD))
    if r.status_code == 201:
        return r
    else:
        raise Exception("Returned status code of {} and returned {}".format(r.status_code, r.json()))

def output():
    '''
    Manage return value of create_repo, providing ssh url.
    '''
    json = create_repo().json()
    ssh_url = json["ssh_url"]
    return "git remote add origin " + ssh_url



if __name__ == '__main__':
    print(output())