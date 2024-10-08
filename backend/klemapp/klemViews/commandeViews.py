from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Commande
from cocoaApp.klemSerializer import CommandeSerializer

class CommandeCreateView(APIView):
    def post(self, request):
        serializer = CommandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommandeListView(generics.ListAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    

class CommandeUpdateView(generics.UpdateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    lookup_field = 'id'  # Utiliser l'ID du Commande pour les opérations

class CommandeDeleteView(generics.DestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    lookup_field = 'id'  # Utiliser l'ID du Commande pour les opérations