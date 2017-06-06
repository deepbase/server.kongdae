from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    
    def __unicode__(self):
        return User.objects.get(pk=self.user_id).name
