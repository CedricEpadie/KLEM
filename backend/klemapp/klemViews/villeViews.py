from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Ville
from cocoaApp.klemSerializer import VilleSerializer

class VilleCreateView(APIView):
    def post(self, request):
        serializer = VilleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VilleListView(generics.ListAPIView):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer
    

class VilleUpdateView(generics.UpdateAPIView):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer
    lookup_field = 'id'  # Utiliser l'ID du Ville pour les opérations

class VilleDeleteView(generics.DestroyAPIView):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer
    lookup_field = 'id'  # Utiliser l'ID du Ville pour les opérations