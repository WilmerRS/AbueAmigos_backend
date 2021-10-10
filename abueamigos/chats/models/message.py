# Django
from django.db import models

# Models
from abueamigos.chats.models.chats import Chat
from abueamigos.utils import AbueAmigosModel


class Message(AbueAmigosModel):
    message = models.CharField(max_length=500)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
