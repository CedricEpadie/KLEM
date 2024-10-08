from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Categorie_article
from cocoaApp.klemSerializer import Categorie_articleSerializer

class Categorie_articleCreateView(APIView):
    def post(self, request):
        serializer = Categorie_articleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Categorie_articleListView(generics.ListAPIView):
    queryset = Categorie_article.objects.all()
    serializer_class = Categorie_articleSerializer
    

class Categorie_articleUpdateView(generics.UpdateAPIView):
    queryset = Categorie_article.objects.all()
    serializer_class = Categorie_articleSerializer
    lookup_field = 'id'  # Utiliser l'ID du Categorie_article pour les opérations

class Categorie_articleDeleteView(generics.DestroyAPIView):
    queryset = Categorie_article.objects.all()
    serializer_class = Categorie_articleSerializer
    lookup_field = 'id'  # Utiliser l'ID du Categorie_article pour les opérations