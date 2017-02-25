from django.shortcuts import render
from musics.models import Music
from musics.serializers import MusicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'musics': reverse('music-list', request=request, format=format)
    })

# Create your views here.
class MusicsViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer