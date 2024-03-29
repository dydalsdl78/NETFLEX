import requests
import json


def pingpong(query):
    header = {
        "Authorization": "Basic a2V5OjA2YWIwYzUyZWVjODIyNzdiMmRmZDkwZTg0YjBlNGE3",
        "Content-Type": "application/json"
    }

    params = {
        "request": {
            "query": "{}".format(query)
        }
    }

    sessionId = "22w42o7e6o5rbxh2urxnyonlbxof1wev"
    url = "https://builder.pingpong.us/api/builder/5fa35802e4b07b8420a5822d/integration/v0.2/custom/" + sessionId

    response = requests.post(url, data=json.dumps(params), headers=header)

    data = response.json()
    ans = data.get('response').get('replies')[0].get('text')
    return ans
