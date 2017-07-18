from __future__ import unicode_literals

from django.db import models

from kongdae.settings import DEBUG
from musics.data.Composer import getComposers
from musics.data.Genre import getGenres
from musics.data.Instrument import getInstruments
from reviews.models import Review, StarRate


COMPOSERS = [(item, getComposers()[item][1]) for item in getComposers()]
GENRES = [(item, getGenres()[item][1]) for item in getGenres()]
INSTRUMENTS = [(item, getInstruments()[item][1]) for item in getInstruments()]
IMG_ROOT_PATH = ""

if DEBUG :
    IMG_ROOT_PATH = "localhost:8000/static/musics/img/"
else :
    IMG_ROOT_PATH = "kongnamul.pythonanywhere.com/static/musics/img/"

# Create your models here.

class Music(models.Model):
    composer = models.CharField(choices=COMPOSERS, max_length=50)
    name = models.CharField(max_length=50)
    koreanName = models.CharField(max_length=50)
    genre = models.CharField(choices=GENRES, max_length=20)
    instrument = models.CharField(choices=INSTRUMENTS, max_length=20, null=True)
    compositionYear = models.IntegerField(blank=True, null=True)
    imageUrl = models.CharField(max_length=100, default=IMG_ROOT_PATH)
    
    def __str__(self): # for python 3.x
        return self.name
    
    def __unicode__(self): # for python 2.7
        return self.name
    
    def getComposer(self):
        return self.composer
    
class MusicReview(Review):
    music = models.ForeignKey(Music)
    
class MusicStarRate(StarRate):
    music = models.ForeignKey(Music)
    
    def __str__(self): # for python 3.x
        return Music.objects.get(pk=self.music_id).title
    
    def __unicode__(self): # for python 2.7
       return Music.objects.get(pk=self.music_id).title
    
    