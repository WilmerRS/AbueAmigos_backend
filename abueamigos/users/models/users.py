from django.db import models
from django.contrib.auth.models import AbstractUser
from abueamigos.utils import AbueAmigosModel


class User(AbueAmigosModel, AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

