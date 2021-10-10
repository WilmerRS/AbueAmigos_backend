# Django
from django.db import models

# Models
from abueamigos.users.models.users import User
from abueamigos.utils import AbueAmigosModel


class ConversationsRequest(AbueAmigosModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
