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


ENDPOINT = "http://127.0.0.1:8000/api/posts/13/"

r = requests.delete(ENDPOINT, headers=headers)
print("Delete Response:", r.status_code)

if r.status_code !=204:
    print("Delete Response Message:", r.json())

