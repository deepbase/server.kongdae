from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.db import models

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    
    def __str__(self):
        return User.objects.get(pk=self.user_id).name
