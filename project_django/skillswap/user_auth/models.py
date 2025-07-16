
from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank= True)
    availability = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"