import json 
import requests 


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

headers = {
    "Content-Type": "application/json",
}

data = {
    'username': 'test5',
    'email':'test5@test.com',
    'password': 'TestPassword',
    'password2': 'TestPassword',
}


r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()
print(token)