from rest_framework import viewsets
from klemapp.models import Article_tag
from klemapp.klemSerializer import Article_tagSerializer

class Article_tagViewSet(viewsets.ModelViewSet):
    queryset = Article_tag.objects.all()
    serializer_class = Article_tagSerializer