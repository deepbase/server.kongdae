from django.contrib import admin

from reviews.models import Review, StarRate, Like

# Register your models here.
admin.site.register(Review)
admin.site.register(StarRate)
admin.site.register(Like)