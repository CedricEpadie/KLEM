from rest_framework import viewsets
from klemapp.models import Mode_Paiement
from klemapp.klemSerializer import Mode_PaiementSerializer

class Mode_PaiementViewSet(viewsets.ModelViewSet):
    queryset = Mode_Paiement.objects.all()
    serializer_class = Mode_PaiementSerializer