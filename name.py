import json


with open('sample-json-file.json', 'r') as file:
    json_data = json.load(file)

for user in json_data['users']:
    print(f"First Name: {user['firstName']}, Last Name: {user['lastName']}")
