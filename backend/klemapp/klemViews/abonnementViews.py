from rest_framework import viewsets
from klemapp.models import Abonnement
from klemapp.klemSerializer import AbonnementSerializer

class AbonnementViewSet(viewsets.ModelViewSet):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer