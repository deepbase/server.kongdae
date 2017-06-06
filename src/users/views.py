from django.contrib.auth.models import User
from rest_framework import viewsets

from reviews.models import Review
from reviews.serializers import ReviewSerializer
from users.serializers import UserSerializer

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        userId = self.kwargs['userId']
        return Review.objects.filter(user = userId);
    