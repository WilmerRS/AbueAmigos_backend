# Django restframework
from rest_framework import serializers

# Models
from abueamigos.users.models.profiles import Profile

# Serializers
from abueamigos.users.serializers.users import UserSerializer


class ConversationRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_field = ['user', ]
