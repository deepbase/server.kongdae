'''
Created on 2017. 2. 25.

@author: Joonki
'''
from musics.models import Music, MusicReview
from rest_framework import serializers

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ('id','composer','name', 'koreanName', 'genre', 'instrument','compositionYear')
        
class MusicReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicReview
        fields = ('id','user','music','type','registeredDateTime','updatedDateTime','title','content', 'likeUsers')