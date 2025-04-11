from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phrase = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'phrase']
    USERNAME_FIELD = 'username'  # or use email if you prefer