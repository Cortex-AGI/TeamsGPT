import requests
import json
import time

with open('./secrets.json', 'r') as file:
    secrets = json.loads(file.read())

class API:
    def __init__(self, dataLoc):
        with open(dataLoc, 'r') as file:
            self.data = json.loads(file.read())
            self.dataLoc = dataLoc

    def getToken(self):
        for i in range(3):
            try:
                if (time.time() >= self.data["time"] + self.data["expires_in"]): # If token has expired
                    code = self.data["refresh_token"]
                    scopes = self.data["scope"]

                    postData = "client_id=" + secrets["MS.client_id"] + "&client_secret=" + secrets["MS.client_secret"] + "&grant_type=refresh_token&scope=" + scopes + "&refresh_token=" + code
                    response = requests.post("https://login.microsoftonline.com/" + secrets["MS.tenant"] + "/oauth2/v2.0/token", data=postData)

                    with open(self.dataLoc, 'w') as file:
                        tokenData = json.loads(str(response.content, encoding='utf-8'))
                        tokenData["time"] = time.time()
                        file.write(json.dumps(tokenData, indent=2))
                        self.data = tokenData

                return self.data["token_type"] + ' ' + self.data["access_token"]
            except:
                pass
    
    def get(self, url, headers={}, **kwargs):
        for i in range(3):
            try:
                requestHeaders = {
                    "Authorization": self.getToken()
                }
                requestHeaders.update(headers)

                response = requests.get(url, headers=requestHeaders, **kwargs)
                return(json.loads(str(response.content, encoding='utf-8')))
            except:
                pass
    
    def post(self, url, headers={}, **kwargs):
        for i in range(3):
            try:
                requestHeaders = {
                    "Authorization": self.getToken()
                }
                requestHeaders.update(headers)

                response = requests.post(url, headers=requestHeaders, **kwargs)
                try:
                    return(json.loads(str(response.content, encoding='utf-8')))
                except:
                    return(response.content)
            except:
                pass