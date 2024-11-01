from rest_framework import viewsets
from klemapp.models import Commentaire
from klemapp.klemSerializer import CommentaireSerializer

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    