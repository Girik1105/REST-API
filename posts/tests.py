import os 
import tempfile
from PIL import Image

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# Create your tests here.
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Post

class StatusAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='Test_Person', email='test_person@test.com')
        user.set_password('Yes_Test_123')
        user.save()

        post_obj = Post.objects.create(user=user, content='Hiiiiii!!!!')
    
    def test_users(self):
        qs = User.objects.filter(username='Test_Person')
        self.assertEqual(qs.count(), 1)

    def test_post(self):
        qs = Post.objects.all()
        self.assertEqual(qs.count(), 1)

    def authenticate_user(self):
        self.test_user = User.objects.get(username='Test_Person')
        self.test_user_pwd = 'Yes_Test_123'
        self.client.force_authenticate(user=self.test_user)

    def test_post_create(self):
        self.authenticate_user()
        url = api_reverse('posts:post-list-create')

        data = {
            'content':"Some test content",
        }
        
        response = self.client.post(url, data, format='json')
        print(response.data, "\nPost status code:", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_post_crud(self):
        self.authenticate_user()
        url = api_reverse('posts:post-list-create')
        data = {
            'content':"This content is about to undergo some crud",
        }
        
        response = self.client.post(url, data, format='json')

        print(response.data, "\nPost CRUD Status code:", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data_id = response.data.get("id")
        url2 = api_reverse('posts:post-detail-delete', kwargs={"id":data_id})

        data2 = {
            'content':"Some test content that is edited!",
        }
        
        # Update
        response2 = self.client.put(url2, data2, format='json')
        print(response2.data, "\nPost Edit status code:", response2.status_code)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

        # Delete
        response3 = self.client.delete(url2, format='json')
        print("\nPost Delete status code:", response3.status_code)
        self.assertEqual(response3.status_code, status.HTTP_204_NO_CONTENT)

        # Not found 
        response4 = self.client.get(url2, format='json')
        print("\nPost Not found status:", response4.status_code)
        self.assertEqual(response4.status_code, status.HTTP_404_NOT_FOUND)

    # def test_post_create_image(self):
    #     self.authenticate_user()
    #     url = api_reverse('posts:post-list-create')

    #     image_item = Image.new('RGB', (100, 100), (55, 247, 255))
    #     temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')   # creating a temporary file in memory to work with
    #     image_item.save(temp_file, format='JPEG')

    #     with open(temp_file.name, 'rb') as file_obj:
    #         data = {
    #             'content':"This is an image test post",
    #             'image': file_obj
    #         }
            
    #         response = self.client.post(url, data, format='multipart')
    #         print(response.data, "\nPost status code:", response.status_code)
    #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)