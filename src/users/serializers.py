'''
Created on 2017. 2. 25.

@author: Joonki
'''
from django.contrib.auth.models import User
from rest_framework import serializers

from reviews.models import Review

class UserSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'reviews')
