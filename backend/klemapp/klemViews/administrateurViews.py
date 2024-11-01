from rest_framework import viewsets
from klemapp.models import Administrateur
from klemapp.klemSerializer import AdministrateurSerializer

class AdministrateurViewSet(viewsets.ModelViewSet):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer