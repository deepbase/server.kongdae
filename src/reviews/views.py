from rest_framework import viewsets, permissions

from kongdae.permissions import IsOwnerOrReadOnly
from reviews.models import Review
from reviews.serializers import ReviewSerializer

# Create your views here.
class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)