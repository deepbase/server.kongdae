from rest_framework import viewsets

from musics.models import Music, MusicReview
from musics.serializers import MusicSerializer, MusicReviewSerializer

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'musics': reverse('music-list', request=request, format=format)
#     })
# Create your views here.
class MusicsViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()
    
class MusicReviewViewSet(viewsets.ModelViewSet):
    serializer_class = MusicReviewSerializer
    queryset = MusicReview.objects.all()
    
class MusicReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = MusicReviewSerializer
    
    def get_queryset(self):
        musicId = self.kwargs['musicId']
        return MusicReview.objects.filter(music = musicId);