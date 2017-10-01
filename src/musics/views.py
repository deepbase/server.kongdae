from rest_framework import viewsets, permissions

from kongdae.permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly
from musics.models import Music, MusicReview
from musics.serializers import MusicSerializer, MusicReviewSerializer

# Create your views here.
class MusicsViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()
    permission_classes = (IsStaffOrReadOnly,)
    
class MusicReviewViewSet(viewsets.ModelViewSet):
    serializer_class = MusicReviewSerializer
    queryset = MusicReview.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    
class MusicReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = MusicReviewSerializer
    
    def get_queryset(self):
        musicId = self.kwargs['musicId']
        return MusicReview.objects.filter(music = musicId);