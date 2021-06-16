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
    "content":"AMAZING POST",
}

ENDPOINT = "http://127.0.0.1:8000/api/posts/6/"

r = requests.put(ENDPOINT, data=json.dumps(post_data), headers=headers)
print("Update Response:", r.status_code, r.json())

if r.status_code != 204:
    print("Update Response Message:")

