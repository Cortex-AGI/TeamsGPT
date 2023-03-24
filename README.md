# GPTeams

This program lets you connect your Microsoft account to ChatGPT, allowing it to reply to your Teams DMs!

This is highly configurable and lets you enter userIDs to reply to, whilst it ignores all the others

## How does it work?
Using the MS Graph API, it retrieves user messages, then filters the unread ones by user ID (specified in config)<br/>
If it matches a "target", then it sends it to the ChatGPT API, with past conversation context, and then generates+sends a response

## Requirements
Relies on Python 3.9+

Install the required dependencies via:
~~~bash
pip3 install -r ./requirements.txt
~~~

## Setup
NOTE: Currently this only works with enterprise or educational Microsoft Accounts as personal ones do not offer the APIs used

1. Create an OpenAI account and get an API Key [here](https://platform.openai.com/account/api-keys)
2. Register a new app [here](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps)
3. Add a redirect URI with platform set to `Web` and URI set to `http://localhost:5000/loggedIn`
4. Under the `Certificates & Secrets` section, create a new client secret
5. Create a `secrets.json` file with the following contents:
~~~json
{
    "AI.api_key": "[API Key from OpenAI]",
    "MS.client_id": "[MS Application ID]",
    "MS.client_secret": "[MS Client Secret]",
    "MS.tenant": "[MS Tenant ID]"
}
~~~
5. Run `sign-in.py` and click on the link shown in the terminal and follow the instructions, once you see `You are now signed in! (You can stop running the program now)` quit the program
6. Run `listChats.py`
7.
Create a `config.json` file with the following contents:
~~~json
{
    "targetUserIDs": []
}
~~~
8. Add the target UserIDs from the members lists supplied by `listChats.py`
9. Run `main.py`
10. Enjoy!
