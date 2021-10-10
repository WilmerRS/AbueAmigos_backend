# Django restframework
from rest_framework import serializers

# Models
from abueamigos.chats.models.chats import Chat
from abueamigos.users.models.users import User

# Serializers
from abueamigos.users.serializers.users import UserSerializer


class ChatSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    contact = serializers.CharField()

    class Meta:
        model = Chat
        fields = "__all__"
        read_only_field = ['user', 'contact']

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data.pop('user'))
        contact = User.objects.get(pk=validated_data.pop('contact'))
        if not user or not contact:
            raise serializers.ValidationError('User or contact invalid.')
        chat, created = Chat.objects.update_or_create(**validated_data, user=user, contact=contact)
        return chat
