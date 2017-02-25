'''
Created on 2017. 2. 25.

@author: Joonki
'''
from musics.models import Music
from rest_framework import serializers

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ('numberOfGradings','sumOfGrades','composer','name','genre','compositionYear')
