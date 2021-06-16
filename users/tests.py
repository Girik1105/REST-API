from rest_framework.test import APITestCase

from rest_framework.reverse import reverse as api_reverse

from rest_framework import status

# Create your tests here.
from django.contrib.auth import get_user_model
User = get_user_model()

class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='Test_Person', email='test_person@test.com')
        user.set_password('Yes_Test_123')
        user.save()
    
    def test_created_user(self):
        qs = User.objects.filter(username='Test_Person')
        self.assertEqual(qs.count(), 1)
    
    def test_created_user_api(self):
        url = api_reverse('user-register')
        data = {
            'username': 'Test_Person_2',
            'email':'Test_123@test.com',
            'password': 'test123',
            'password2': 'test123',            
        }
        response = self.client.post(url, data, format='json')
        print(response.data, "\nStatus:",response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user_api(self):
        url = api_reverse('user-login')
        data = {
            'username': 'Test_Person', #use the already created one
            'password': 'Yes_Test_123',           
        }
        response = self.client.post(url, data, format='json')
        print(response.data, "\nStatus:",response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_login_user_api(self):
        url = api_reverse('user-login')
        data = {
            'username': 'Test_Person', #use the already created one
            'password': 'Yes_Test_123',           
        }
        response = self.client.post(url, data, format='json')
        print(response.data, "\nStatus:",response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='JWT' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
