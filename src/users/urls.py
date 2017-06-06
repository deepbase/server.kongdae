from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from users.views import UsersViewSet, UserReviewsViewSet

users = UsersViewSet.as_view({
    'get': 'list',
    'post': 'create'                                    
})

user = UsersViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

userReviews = UserReviewsViewSet.as_view({
    'get': 'list'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', users, name='users'),
    url(r'^(?P<pk>[0-9]+)/$', user, name='user'),
    url(r'^(?P<userId>[0-9]+)/reviews/$', userReviews, name='userReviews'),
])
