from rest_framework import viewsets
from klemapp.models import Souscription
from klemapp.klemSerializer import SouscriptionSerializer

class SouscriptionViewSet(viewsets.ModelViewSet):
    queryset = Souscription.objects.all()
    serializer_class = SouscriptionSerializer