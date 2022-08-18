from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    """Base user model plus unique email, phone, image, city"""
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = PhoneNumberField(unique=True, null=False, blank=True)
    city = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatar/', blank=False, null=True, default='avatar/Billy.jpg')

    REQUIRED_FIELDS = ['email', 'city', ]

    def __str__(self):
        return self.username
