# Django restframework
from rest_framework import serializers

# Models
from abueamigos.chats.models.conversation_requests import ConversationsRequest
from abueamigos.users.models.users import User

# Serializers
from abueamigos.users.serializers.users import UserSerializer


class ConversationRequestSerializer(serializers.ModelSerializer):
    user = serializers.CharField()

    class Meta:
        model = ConversationsRequest
        fields = "__all__"
        read_only_field = ['user']

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data.pop('user'))
        convesations, created = ConversationsRequest.objects.update_or_create(**validated_data, user=user)
        return convesations


class ListConversationRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ConversationsRequest
        fields = "__all__"
        read_only_field = ['user']
