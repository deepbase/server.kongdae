'''
Created on 2017. 6. 6.

@author: Joonki
'''
from rest_framework import serializers

from reviews.models import Review, Like, Comment

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.userame')
    
    class Meta:
        model = Review
        fields = ('id','user','type','registeredDateTime','updatedDateTime','title','content', 'likeUsers')
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('review','user','registeredDateTime')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('review','user','content','registeredDateTime')