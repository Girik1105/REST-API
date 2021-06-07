from typing import ValuesView
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

headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

post_data = {
    "content":"New Post",
}

ENDPOINT = "http://127.0.0.1:8000/api/posts/"

r = requests.get(ENDPOINT, headers=headers)

items = r.json()


for item in items:
    for field, value in item.items():
        print(field, value)