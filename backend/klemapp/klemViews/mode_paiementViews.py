from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Mode_Paiement
from cocoaApp.klemSerializer import Mode_PaiementSerializer

class Mode_PaiementCreateView(APIView):
    def post(self, request):
        serializer = Mode_PaiementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Mode_PaiementListView(generics.ListAPIView):
    queryset = Mode_Paiement.objects.all()
    serializer_class = Mode_PaiementSerializer
    

class Mode_PaiementUpdateView(generics.UpdateAPIView):
    queryset = Mode_Paiement.objects.all()
    serializer_class = Mode_PaiementSerializer
    lookup_field = 'id'  # Utiliser l'ID du Mode_Paiement pour les opérations

class Mode_PaiementDeleteView(generics.DestroyAPIView):
    queryset = Mode_Paiement.objects.all()
    serializer_class = Mode_PaiementSerializer
    lookup_field = 'id'  # Utiliser l'ID du Mode_Paiement pour les opérations