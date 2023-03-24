from flask import Flask, request
import requests
import json
import time

with open('./secrets.json', 'r') as file:
    secrets = json.loads(file.read())

app = Flask(__name__)
scopes = "Chat.Create%20Chat.Read%20Chat.ReadBasic%20Chat.ReadWrite%20ChatMessage.Read%20ChatMessage.Send%20TeamsAppInstallation.ReadForChat%20User.Read%20User.ReadBasic.All%20User.ReadWrite%20offline_access"

@app.route("/loggedIn")
def logined():
    code = str(request.query_string, encoding='utf-8').split('&')[0].split('code=')[-1]

    postData = "client_id=" + secrets["MS.client_id"] + "&client_secret=" + secrets["MS.client_secret"] + "&grant_type=authorization_code&redirect_uri=http%3A%2F%2Flocalhost:5000%2FloggedIn&scope=" + scopes + "&code=" + code
    response = requests.post("https://login.microsoftonline.com/" + secrets["MS.tenant"] + "/oauth2/v2.0/token", data=postData)

    #token = json.loads(str(response, encoding='utf-8'))["token_type"] + ' ' + json.loads(str(response, encoding='utf-8'))["access_token"]
    with open('./tokens.json', 'w') as file:
        tokenData = json.loads(str(response.content, encoding='utf-8'))
        tokenData["time"] = time.time()
        file.write(json.dumps(tokenData, indent=2))

    return "You are now signed in! (You can stop running the program now)"


print("\n\nLogin URL:")
print("https://login.microsoftonline.com/" + secrets["MS.tenant"] + "/oauth2/v2.0/authorize?client_id=" + secrets["MS.client_id"] + "&response_type=code&redirect_uri=http%3A%2F%2Flocalhost:5000%2FloggedIn&response_mode=query&scope=" + scopes)
print("\n\n")

app.run(debug=True)