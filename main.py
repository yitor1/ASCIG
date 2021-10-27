import os
import random
import requests
import json

url = "https://pastebin.com/raw/BhV66L56"

try:
    idea_list_request = requests.get(url)
    idea_list = idea_list_request.json()
except:
    print("An error has occurred")

print("Character age : " + idea_list["character_age"][random.randint(0, len(idea_list["character_age"]) - 1)])
print("Character type : " + idea_list["character_type"][random.randint(0, len(idea_list["character_type"]) - 1)])
print("Character type (optional) : " + idea_list["character_type_optional"][random.randint(0, len(idea_list["character_type_optional"]) - 1)])
print("Character role : " + idea_list["character_role"][random.randint(0, len(idea_list["character_role"]) - 1)])
print("Character gender (optional): " + idea_list["character_gender"][random.randint(0, len(idea_list["character_gender"]) - 1)])
