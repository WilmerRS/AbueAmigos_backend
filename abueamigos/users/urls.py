# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from abueamigos.users.views.users import Users

router = DefaultRouter()
router.register(r'users', Users, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
