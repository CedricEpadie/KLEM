from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from klemapp.models import Abonnement
from klemapp.klemSerializer import AbonnementSerializer

class AbonnementCreateView(APIView):
    def post(self, request):
        serializer = AbonnementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AbonnementListView(generics.ListAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer

class AbonnementUpdateView(generics.UpdateAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    lookup_field = 'id'  # Utiliser l'ID du Abonnement pour les opérations

class AbonnementDeleteView(generics.DestroyAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    lookup_field = 'id'  # Utiliser l'ID du Abonnement pour les opérations