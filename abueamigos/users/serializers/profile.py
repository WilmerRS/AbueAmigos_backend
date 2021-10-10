# Django
from django.contrib.auth.hashers import make_password

# Django restframework
from rest_framework import serializers

# Models
from abueamigos.users.models.profiles import Profile

# Serializers
from abueamigos.users.serializers.users import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.password = make_password(user.password)
        profile, created = Profile.objects.update_or_create(**validated_data, user=user)
        return profile
