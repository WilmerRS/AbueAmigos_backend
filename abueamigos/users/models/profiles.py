# Django
from django.db import models

# Models
from abueamigos.users.models.users import User
from abueamigos.utils import AbueAmigosModel


class Profile(AbueAmigosModel):
    phone_number = models.CharField(max_length=20)
    reputation = models.FloatField(default=5.0)
    picture = models.ImageField('profile picture',
                                upload_to='users/pictures/',
                                blank=True,
                                null=True)
    biography = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
