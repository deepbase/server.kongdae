from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from musics.views import MusicsViewSet, MusicReviewsViewSet, MusicReviewViewSet

musics = MusicsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

music = MusicsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

musicReviews = MusicReviewsViewSet.as_view({
    'get': 'list'
})

allMusicReviews = MusicReviewViewSet.as_view({
    'get': 'list'
})

musicReview = MusicReviewViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', musics, name='musics'),
    url(r'^(?P<pk>[0-9]+)/$', music, name='music'),
    url(r'^(?P<musicId>[0-9]+)/reviews/$', musicReviews, name='musicReviews'),
    url(r'^reviews/$', allMusicReviews, name='allMusicReviews'),
    url(r'^reviews/(?P<pk>[0-9]+)/$', musicReview, name='musicReview'),
])
