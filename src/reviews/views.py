from rest_framework import viewsets, permissions

from kongdae.permissions import IsOwnerOrReadOnly
from reviews.models import Review, Comment
from reviews.serializers import ReviewSerializer, CommentSerializer

# Create your views here.
class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    
class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_queryset(self):
        reviewId = self.kwargs['reviewId']
        return Comment.objects.filter(review = reviewId)