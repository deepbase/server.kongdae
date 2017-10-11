from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

APPS = [('musics', 'musics'), ('musicians', 'musicians'), ('concerts', 'concerts')]

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    userNickname = models.CharField(max_length=50)
    type = models.CharField(choices=APPS, max_length=10, null=True)
    registeredDateTime = models.DateTimeField(auto_now_add=True)
    updatedDateTime = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    images = models.ImageField
    likeUsers = models.ManyToManyField(User, blank=True, related_name='likeUsers', through='Like')
    commentUsers = models.ManyToManyField(User, blank=True, related_name='commentUsers', through='Comment')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def __str__(self):
        return self.title
    
    def __unicode__(self): # for python 2.7
        return self.title
    
class StarRate(models.Model):
    user = models.ForeignKey(User)
    rate = models.IntegerField(blank=True, null=True)
    
# Mediator
class Like(models.Model):
    review = models.ForeignKey(Review)
    user = models.ForeignKey(User)
    registeredDateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return Review.objects.get(pk=self.review_id).title
    
    def __unicode__(self):
        return Review.objects.get(pk=self.review_id).title
    
class Comment(models.Model):
    review = models.ForeignKey(Review)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=200)
    registeredDateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return Review.objects.get(pk=self.review_id).title
    
    def __unicode__(self):
        return Review.objects.get(pk=self.review_id).title