from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from klemapp.models import Pays
from klemapp.klemSerializer import PaysSerializer

class PaysCreateView(APIView):
    def post(self, request):
        serializer = PaysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PaysListView(generics.ListAPIView):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer
    

class PaysUpdateView(generics.UpdateAPIView):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer
    lookup_field = 'id'  # Utiliser l'ID du Pays pour les opérations

class PaysDeleteView(generics.DestroyAPIView):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer
    lookup_field = 'id'  # Utiliser l'ID du Pays pour les opérations