from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from klemapp.models import Pays
from klemapp.klemSerializer import PaysSerializer

class PaysViewSet(viewsets.ModelViewSet):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer