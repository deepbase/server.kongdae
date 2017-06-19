from __future__ import unicode_literals

from django.db import models

from musics.data.Composer import getComposers
from musics.data.Genre import getGenres
from musics.data.Instrument import getInstruments
from reviews.models import Review, StarRate

COMPOSERS = [(item, getComposers()[item][1]) for item in getComposers()]
GENRES = [(item, getGenres()[item][1]) for item in getGenres()]
INSTRUMENTS = [(item, getInstruments()[item][1]) for item in getInstruments()]

# Create your models here.

class Music(models.Model):
    composer = models.CharField(choices=COMPOSERS, max_length=50)
    name = models.CharField(max_length=50)
    koreanName = models.CharField(max_length=50)
    genre = models.CharField(choices=GENRES, max_length=20)
    instrument = models.CharField(choices=INSTRUMENTS, max_length=20, null=True)
    compositionYear = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class MusicReview(Review):
    music = models.ForeignKey(Music)
    
class MusicStarRate(StarRate):
    music = models.ForeignKey(Music)
    
    def __unicode__(self):
        return Music.objects.get(pk=self.music_id).title