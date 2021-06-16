import requests
import json

AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/'

user_data = {
    'username':'girik',
    'password':'TestPassword'
}

headers = {
    "Content-Type": "application/json",
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(user_data), headers=headers)
token = r.json()['token']

print('Authorization call:', r.status_code)
print('JWT TOken Recieved:', token)

headers2 = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

post_data = {
    'content': 'this new content post 2 from api call'
}

ENDPOINT = "http://127.0.0.1:8000/api/posts/"

r = requests.post(ENDPOINT, data=post_data, headers=headers2)
print("Create Response:", r.status_code)
print(r.json())
