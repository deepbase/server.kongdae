from django.conf.urls import url
from django.contrib import admin
from musics.views import MusicsViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns

musics_list = MusicsViewSet.as_view({
    'get': 'list',
    'post': 'create'                                    
})

musics_detail = MusicsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^musics/$', musics_list, name='music-list'),
    url(r'^musics/(?P<pk>[0-9]+)/$', musics_detail, name='music-detail')
])
