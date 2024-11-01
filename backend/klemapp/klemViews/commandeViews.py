from rest_framework import viewsets
from klemapp.models import Commande
from klemapp.klemSerializer import CommandeSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer