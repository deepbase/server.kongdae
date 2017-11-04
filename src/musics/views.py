from rest_framework import viewsets, permissions

from kongdae.permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly
from musics.models import Music, MusicReview
from musics.serializers import MusicSerializer, MusicReviewSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MusicsViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()
    permission_classes = (IsAuthenticated, IsStaffOrReadOnly,)
    
    def get_queryset(self):
        queryset = Music.objects.all()
        composerParam = self.request.query_params.get('composer', None)
        compositionYearParam = self.request.query_params.get('compositionYear', None)
        genreParam = self.request.query_params.get('genre', None)
        instrumentParam = self.request.query_params.get('instrument', None)
        if composerParam is not None:
            queryset = queryset.filter(composer=composerParam)
        if compositionYearParam is not None:
            queryset = queryset.filter(compositionYear=compositionYearParam)
        if genreParam is not None:
            queryset = queryset.filter(genre=genreParam)
        if instrumentParam is not None:
            queryset = queryset.filter(instrument=instrumentParam)
        return queryset
    
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