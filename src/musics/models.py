from __future__ import unicode_literals

from django.db import models
from data import Composer
from musics.data.Composer import getComposers

# Create your models here.

class Music(models.Model):
    numberOfGradings = models.IntegerField
    sumOfGrades = models.IntegerField
    composer = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    compositionYear = models.IntegerField
    image = models.ImageField
