from rest_framework import viewsets
from klemapp.models import Article
from klemapp.klemSerializer import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer