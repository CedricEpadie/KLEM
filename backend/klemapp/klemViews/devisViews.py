from rest_framework import viewsets
from klemapp.models import Devis
from klemapp.klemSerializer import DevisSerializer

class DevisViewSet(viewsets.ModelViewSet):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer