from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from abueamigos.chats.models.chats import Chat
from abueamigos.chats.models.message import Message

# Serializers
from abueamigos.chats.serializers.chats import ChatSerializer
from abueamigos.chats.serializers.messages import ListMessageSerializer


class ChatsViews(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 # mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    @action(methods=['get'], detail=False)
    def messages(self, request, pk=None):
        user = request.query_params['user']
        contact = request.query_params['contact']
        print(user, contact)
        if not user or not contact:
            return Response('Error: Not user or contact for the conversation', 400)

        chats = Chat.objects.filter(user__pk=user, contact__pk=contact)
        if len(chats) == 0:
            chats = Chat.objects.filter(user__pk=contact, contact__pk=user)

        messages = Message.objects.filter(chat=chats)
        serializer = ListMessageSerializer(data=messages)
        if serializer.is_valid():
            return Response('Messages is not valid.', 400)
        return Response(serializer.data)
