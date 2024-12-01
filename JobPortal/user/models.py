
from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=255, default="")
    email = models.EmailField(unique=True,default="")
    phone_number = models.CharField(max_length=15, default="")
    age = models.PositiveIntegerField()
    address = models.TextField(default="")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    password = models.CharField(max_length=255,default="")

    def __str__(self):
        return self.full_name
