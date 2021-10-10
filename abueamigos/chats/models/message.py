# Django
from django.db import models

# Models
from abueamigos.utils import AbueAmigosModel
from abueamigos.chats.models.chats import Chat
from abueamigos.users.models.users import User


class Message(AbueAmigosModel):
    message = models.CharField(max_length=500)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transmitter')

