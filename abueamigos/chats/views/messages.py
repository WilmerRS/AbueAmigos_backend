from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from abueamigos.chats.models.message import Message

# Serializers
from abueamigos.chats.serializers.messages import MessageSerializer


class MessageViews(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
