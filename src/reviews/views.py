from rest_framework import viewsets

from reviews.models import Review
from reviews.serializers import ReviewSerializer

# Create your views here.
class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer