from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from klemapp.models import Commentaire
from klemapp.klemSerializer import CommentaireSerializer

class CommentaireCreateView(APIView):
    def post(self, request):
        serializer = CommentaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentaireListView(generics.ListAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    

class CommentaireUpdateView(generics.UpdateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    lookup_field = 'id'  # Utiliser l'ID du Commentaire pour les opérations

class CommentaireDeleteView(generics.DestroyAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    lookup_field = 'id'  # Utiliser l'ID du Commentaire pour les opérations