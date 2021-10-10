# Django restframework
from rest_framework import serializers

# Models
from abueamigos.chats.models.chats import Chat

# Serializers
from abueamigos.users.serializers.users import UserSerializer


class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    contact = UserSerializer()

    class Meta:
        model = Chat
        fields = "__all__"
        read_only_field = ['user', 'contact']
