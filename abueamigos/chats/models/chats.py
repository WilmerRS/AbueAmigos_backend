# Django
from django.db import models

# Models
from abueamigos.users.models.users import User
from abueamigos.utils import AbueAmigosModel


class Chat(AbueAmigosModel):
    full_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact')
    last_message = models.CharField(max_length=500)
