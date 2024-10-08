from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Administrateur
from cocoaApp.klemSerializer import AdministrateurSerializer

class AdministrateurCreateView(APIView):
    def post(self, request):
        serializer = AdministrateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdministrateurListView(generics.ListAPIView):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer
    

class AdministrateurUpdateView(generics.UpdateAPIView):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer
    lookup_field = 'id'  # Utiliser l'ID du Administrateur pour les opérations

class AdministrateurDeleteView(generics.DestroyAPIView):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer
    lookup_field = 'id'  # Utiliser l'ID du Administrateur pour les opérations