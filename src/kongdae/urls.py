from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^musics/', include('musics.urls', namespace="musics")),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls))
]
