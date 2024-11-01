from rest_framework import viewsets
from klemapp.models import Tag
from klemapp.klemSerializer import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer