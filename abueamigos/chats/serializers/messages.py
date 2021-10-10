# Django restframework
from rest_framework import serializers

# Models
from abueamigos.chats.models.message import Message
from abueamigos.users.models.users import User
from abueamigos.chats.models.chats import Chat

# Serializers
from abueamigos.chats.serializers.chats import ChatSerializer
from abueamigos.users.serializers.users import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    chat = serializers.CharField(allow_null=True)
    user = serializers.CharField()
    contact = serializers.CharField()

    class Meta:
        model = Message
        fields = "__all__"
        read_only_field = ['chat', 'user', 'contact']

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data.pop('user'))
        contact = User.objects.get(pk=validated_data.pop('contact'))
        if not user or not contact:
            raise serializers.ValidationError('User and contact are required')
        chat_id = validated_data.pop('chat')
        message=validated_data.pop('message')
        chat = None
        if not chat_id:
            full_name = user.first_name + ' ' + user.last_name
            chat = Chat.objects.create(user=user, full_name=full_name, contact=contact, last_message=message)
        else:
            chat = Chat.objects.get(pk=chat_id)
            chat.last_message = message
            chat.save()

        message, created = Message.objects.update_or_create(message=message, user=user, chat=chat)
        return message

class ListMessageSerializer(serializers.ModelSerializer):
    chat = ChatSerializer()
    user = UserSerializer()

    class Meta:
        model = Message
        fields = "__all__"
        read_only_field = ['chat', 'user']