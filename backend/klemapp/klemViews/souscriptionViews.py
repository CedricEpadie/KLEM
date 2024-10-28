from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from klemapp.models import Souscription
from klemapp.klemSerializer import SouscriptionSerializer

class SouscriptionCreateView(APIView):
    def post(self, request):
        serializer = SouscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SouscriptionListView(generics.ListAPIView):
    queryset = Souscription.objects.all()
    serializer_class = SouscriptionSerializer
    
class SouscriptionUpdateView(generics.UpdateAPIView):
    queryset = Souscription.objects.all()
    serializer_class = SouscriptionSerializer
    lookup_field = 'id'  # Utiliser l'ID du Souscription pour les opérations

class SouscriptionDeleteView(generics.DestroyAPIView):
    queryset = Souscription.objects.all()
    serializer_class = SouscriptionSerializer
    lookup_field = 'id'  # Utiliser l'ID du Souscription pour les opérations