from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from reviews.views import ReviewsViewSet

reviews_list = ReviewsViewSet.as_view({
    'get': 'list'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', reviews_list, name='review-list'),
])
