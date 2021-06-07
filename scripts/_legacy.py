import requests 
import json 
import os 


ENDPOINT = "http://127.0.0.1:8000/api/posts/3/"


def create_post(data={}, is_json=True):
    headers = {}
    if json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    
    r = requests.request('post', ENDPOINT, data=data, headers=headers)

    return r, r.status_code, r.json()


# check =create_post({"user":1, "content":"sending api calls from script pt2", "image":None})
# print(check)


def create_post_with_img(data={}, is_json=True, img_path=None):
    headers = {}
    if json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    
    if img_path is not None:
        with open(img_path, 'rb') as image:
            file_data = {
                "imae":image
            }  
    r = requests.request('post', ENDPOINT, data=data, files=file_data, headers=headers)

    return r, r.status_code, r.json()

# base = os.getcwd()
# img_path = os.path.join(base, 'beach.jpg')
# check = create_post_with_img({"user":1, 'content':'Post with img'}, is_json=False, img_path=img_path)
# print(check)

def manage_post(method, id, data={}, is_json=True):
    if json:
        data = json.dumps(data)
    
    r = requests.request(method, ENDPOINT + "?id=" + str(id), data=data)

    return r, r.status_code, r.json()

# print(manage_post('get', 3, {"id":3}))

BASE_ENDPOINT = 'http://127.0.0.1:8000/api/posts/'

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

headers = {
    "Content-Type": "application/json",
}

data = {
    'username': 'test2',
    'email':'test2@test.com',
    'password': 'TestPassword',
    'password2': 'TestPassword',
}


# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()
# print(token)


ENDPOINT = 'http://127.0.0.1:8000/api/auth/'

data2 = {
    'username':'girik',
    'password':'TestPassword'
}

r = requests.post(ENDPOINT, data=json.dumps(data2), headers=headers)
token = r.json()['token']
print(r.status_code, token)

headers2 = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

data3 = {
    "content":"HEY THERE, THIS IS AN AUTHORIZED POST",
}

ENDPOINT = "http://127.0.0.1:8000/api/posts/2/"

r = requests.put(ENDPOINT, data=json.dumps(data3), headers=headers2)
print(r.status_code, r, r.json())

r = requests.get(ENDPOINT, headers=headers2)
print(r.json())