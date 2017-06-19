from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

APPS = [('musics', 'musics'), ('musicians', 'musicians'), ('concerts', 'concerts')]

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    type = models.CharField(choices=APPS, max_length=10, null=True)
    registeredDateTime = models.DateTimeField(auto_now_add=True)
    updatedDateTime = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    images = models.ImageField
    likeUsers = models.ManyToManyField(User, blank=True, related_name='likeUsers', through='Like')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def __unicode__(self):
        return self.title
    
class StarRate(models.Model):
    user = models.ForeignKey(User)
    rate = models.IntegerField
    
# Mediator
class Like(models.Model):
    review = models.ForeignKey(Review)
    user = models.ForeignKey(User)
    registeredDateTime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return Review.objects.get(pk=self.review_id).title