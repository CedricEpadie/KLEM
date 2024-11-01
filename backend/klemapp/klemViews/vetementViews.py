from rest_framework import viewsets
from klemapp.models import Vetement
from klemapp.klemSerializer import VetementSerializer

class VetementViewSet(viewsets.ModelViewSet):
    queryset = Vetement.objects.all()
    serializer_class = VetementSerializer