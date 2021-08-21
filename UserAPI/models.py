from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class UserInfo (models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=100)
    diet = models.TextField(blank=True)
    intolerance = models.TextField(blank=True)
    owner = models.ForeignKey(
        User, related_name="userInfo", on_delete=models.CASCADE, null=True)
    favourite1 = models.CharField(max_length=100)
    favourite2 = models.CharField(max_length=100)
    favourite3 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

