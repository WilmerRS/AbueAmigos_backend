from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from abueamigos.chats.models.chats import Chat

# Serializers
from abueamigos.chats.serializers.chats import ChatSerializer


class ChatsViews(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()