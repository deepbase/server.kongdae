from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from reviews.views import ReviewsViewSet

reviews = ReviewsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', reviews, name='reviews'),
])
