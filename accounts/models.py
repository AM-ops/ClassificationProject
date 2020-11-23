from django.db import models
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.
class Person(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "{}".format(self.username)

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)