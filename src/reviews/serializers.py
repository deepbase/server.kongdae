'''
Created on 2017. 6. 6.

@author: Joonki
'''
from rest_framework import serializers

from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('user','type','registeredDateTime','updatedDateTime','title','content', 'likeUsers')