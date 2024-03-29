# REST-API
REST API with Django Rest Framework 

# SETUP AND INSTALLATION 

Download requirements:
```
pip install -r requirements.txt
```
Then run the python file:
```
python manage.py runserver 
```

# Endpoints:

```
/api/posts/
```
Create and List View

```
/api/posts/<post id>/
```
Detail, Update and Delete view

# Auth Endpoints 
```
api/auth/register/
```
To Create Users and get User Tokens 

```
/api/auth/
```
To get JWT Tokens 

```
/api/auth/jwt/verify/
```
To verify jwt tokens 

```
/api/auth/jwt/refresh/
```
To refresh JWT tokens 


# Django Apps 

[users](https://github.com/Girik1105/REST-API/tree/master/users) : Handling all authentication of users

[Posts](https://github.com/Girik1105/REST-API/tree/master/posts) : Model of posts, All CRUDL Views

# Tests

```
python manage.py test
```

[Scripts](https://github.com/Girik1105/REST-API/tree/master/scripts) : Scripts to test the api 
