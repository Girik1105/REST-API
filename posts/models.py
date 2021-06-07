from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="uploads") #django storages for storing in web services like aws
    timestamp =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:15]
    
    @property
    def owner(self):
        return self.user