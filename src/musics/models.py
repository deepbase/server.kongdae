from __future__ import unicode_literals

from django.db import models
from musics.data.Composer import getComposers
from musics.data.Genre import getGenres
from musics.data.Instrument import getInstruments

COMPOSERS = [(item, getComposers()[item][1]) for item in getComposers()]
GENRES = [(item, getGenres()[item][1]) for item in getGenres()]
INSTRUMENTS = [(item, getInstruments()[item][1]) for item in getInstruments()]
# Create your models here.

class Music(models.Model):
    numberOfGradings = models.IntegerField(blank=True, null=True)
    sumOfGrades = models.IntegerField(blank=True, null=True)
    composer = models.CharField(choices=COMPOSERS, max_length=50)
    name = models.CharField(max_length=50)
    genre = models.CharField(choices=GENRES, max_length=20)
    instrument = models.CharField(choices=INSTRUMENTS, max_length=20)
    compositionYear = models.IntegerField(blank=True, null=True)