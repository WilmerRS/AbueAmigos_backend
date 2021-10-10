# Django restframework
from rest_framework import serializers

# Models
from abueamigos.users.models.profiles import Profile

# Serializers
from abueamigos.chats.serializers.chats import ChatSerializer


class MessageSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(required=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_field = ['chat',]
