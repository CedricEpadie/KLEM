from rest_framework import viewsets
from klemapp.models import Ville
from klemapp.klemSerializer import VilleSerializer

class VilleViewSet(viewsets.ModelViewSet):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer