# Django restframework
from rest_framework import serializers

# Models
from abueamigos.chats.models.message import Message

# Serializers
from abueamigos.chats.serializers.chats import ChatSerializer


class MessageSerializer(serializers.ModelSerializer):
    chat = ChatSerializer()

    class Meta:
        model = Message
        fields = "__all__"
        read_only_field = ['chat']
