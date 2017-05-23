from django.contrib.auth.models import User
from django.db import models
from musics.models import Music

# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(User, unique=True)
    likeReviewId = models.ManyToManyField
    
    def __unicode__(self):
        return self.user
    
class Review(models.Model):
    user = models.ForeignKey(User, unique=True)
    registeredDateTime = models.DateTimeField(auto_now_add=True)
    updatedDateTime = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    images = models.ImageField
    likeUsers = models.ManyToManyField(User, null=True, blank=True, related_name='likeUsers', through='Like')
    
    def __unicode__(self):
        return self.title
    
class StarRate(models.Model):
    user = models.ForeignKey(User, unique=True)
    music = models.ForeignKey(Music, unique=True)
    rate = models.IntegerField
    
    def __unicode__(self):
        return self.music
    
# Mediator
class Like(models.Model):
    review = models.ForeignKey(Review,)
    user = models.ForeignKey(User,)
    registeredDateTime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.review