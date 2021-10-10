from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from abueamigos.chats.models.conversation_requests import ConversationsRequest

# Serializers
from abueamigos.chats.serializers.conversation_requests import ConversationRequestSerializer
from abueamigos.chats.serializers.conversation_requests import ListConversationRequestSerializer


class ConversationRequestViews(mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    serializer_class = ConversationRequestSerializer
    queryset = ConversationsRequest.objects.all()
    ordering = ('-created', '-modified')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListConversationRequestSerializer(queryset, many=True)
        return Response(serializer.data)
