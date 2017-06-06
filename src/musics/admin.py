from django.contrib import admin

from musics.models import Music, MusicReview, MusicStarRate

# Register your models here.
admin.site.register(Music)
admin.site.register(MusicReview)
admin.site.register(MusicStarRate)