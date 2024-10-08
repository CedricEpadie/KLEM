from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Article_tag
from cocoaApp.klemSerializer import Article_tagSerializer

class Article_tagCreateView(APIView):
    def post(self, request):
        serializer = Article_tagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Article_tagListView(generics.ListAPIView):
    queryset = Article_tag.objects.all()
    serializer_class = Article_tagSerializer
    

class Article_tagUpdateView(generics.UpdateAPIView):
    queryset = Article_tag.objects.all()
    serializer_class = Article_tagSerializer
    lookup_field = 'id'  # Utiliser l'ID du Article_tag pour les opérations

class Article_tagDeleteView(generics.DestroyAPIView):
    queryset = Article_tag.objects.all()
    serializer_class = Article_tagSerializer
    lookup_field = 'id'  # Utiliser l'ID du Article_tag pour les opérations