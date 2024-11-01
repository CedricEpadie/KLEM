from rest_framework import viewsets
from klemapp.models import Categorie_article
from klemapp.klemSerializer import Categorie_articleSerializer

class Categorie_articleViewSet(viewsets.ModelViewSet):
    queryset = Categorie_article.objects.all()
    serializer_class = Categorie_articleSerializer