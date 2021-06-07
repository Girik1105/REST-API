from django.contrib import admin

from . import models
# Register your models here.

# Adding some customization to the admin 
admin.site.register(models.Post)