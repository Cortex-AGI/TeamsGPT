from msapi import API
import openai
import json

with open('./secrets.json', 'r') as file:
    secrets = json.loads(file.read())
openai.api_key = secrets["AI.api_key"]

api = API('./tokens.json')

# Get user data
userData = api.get("https://graph.microsoft.com/v1.0/me")
userID = userData["id"]

print("Listing chats")
# List chats
chats = api.get("https://graph.microsoft.com/v1.0/me/chats?$expand=members&$top=50")
chatID = ''

for chat in chats["value"]:
    if (len(chat["members"]) != 2):
        continue

    for member in chat["members"]:
        if (member["userId"] != userID):
            print(member["displayName"] + '\t' + member["userId"])