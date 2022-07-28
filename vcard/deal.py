
from requests import request
import requests
import json
# import pprint

with open("./group.json", "r") as json_file:
    group = json.load(json_file)
with open("./contact.json", "r", encoding="utf-8") as json_file:
    contact = json.load(json_file)

contactList = contact["contactList"]
phones=[]
for key in contactList:
    for phone in key["telList"]:
        phones.append(phone["value"])

print(phones)
print(len(phones))