# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from abueamigos.chats.views.conversation_requests import ConversationRequestViews
from abueamigos.chats.views.messages import MessageViews
from abueamigos.chats.views.chats import ChatsViews

router = DefaultRouter()
router.register(r'conversations', ConversationRequestViews, basename='Conversations')
router.register(r'chats', ChatsViews, basename='Chats')
router.register(r'messages', MessageViews, basename='Messages')

urlpatterns = [
    path('', include(router.urls))
]
