from rest_framework import generics
from .models import Info
from .serializers import InfoSerializer


class PostInfoList(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer




class PostInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer