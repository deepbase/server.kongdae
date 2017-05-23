from django.contrib import admin

from users.models import UserInfo, Review, StarRate, Like

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Review)
admin.site.register(StarRate)
admin.site.register(Like)