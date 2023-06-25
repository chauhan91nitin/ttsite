from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class student(AbstractUser):
    
    username = None
    
    phone_number = models.CharField(max_length=50, unique=True)
    stud_email=models.EmailField(unique=True)
    average_marks = models.IntegerField(max_length=100)
    stud_location = models.CharField(max_length=100)

    objects = UserManager

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []