from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Vetement
from cocoaApp.klemSerializer import VetementSerializer

class VetementCreateView(APIView):
    def post(self, request):
        serializer = VetementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VetementListView(generics.ListAPIView):
    queryset = Vetement.objects.all()
    serializer_class = VetementSerializer
    

class VetementUpdateView(generics.UpdateAPIView):
    queryset = Vetement.objects.all()
    serializer_class = VetementSerializer
    lookup_field = 'id'  # Utiliser l'ID du Vetement pour les opérations

class VetementDeleteView(generics.DestroyAPIView):
    queryset = Vetement.objects.all()
    serializer_class = VetementSerializer
    lookup_field = 'id'  # Utiliser l'ID du Vetement pour les opérations