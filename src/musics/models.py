from __future__ import unicode_literals

from django.db import models
from musics.data.Composer import getComposers

COMPOSERS = [(item, item) for item in getComposers()]
# Create your models here.

class Music(models.Model):
    numberOfGradings = models.IntegerField(blank=True, null=True)
    sumOfGrades = models.IntegerField(blank=True, null=True)
    composer = models.CharField(choices=COMPOSERS, max_length=50)
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    compositionYear = models.IntegerField(blank=True, null=True)
    image = models.ImageField(null=True)
