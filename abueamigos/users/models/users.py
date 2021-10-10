from django.db import models
from django.contrib.auth.models import AbstractUser
from abueamigos.utils import AbueAmigosModel


class User(AbueAmigosModel, AbstractUser):
    pass

