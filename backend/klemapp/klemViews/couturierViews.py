from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from klemapp.models import Couturier
from klemapp.klemSerializer import CouturierSerializer

class CouturierCreateView(APIView):
    def post(self, request):
        serializer = CouturierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CouturierListView(generics.ListAPIView):
    queryset = Couturier.objects.all()
    serializer_class = CouturierSerializer
    

class CouturierUpdateView(generics.UpdateAPIView):
    queryset = Couturier.objects.all()
    serializer_class = CouturierSerializer
    lookup_field = 'id'  # Utiliser l'ID du Couturier pour les opérations

class CouturierDeleteView(generics.DestroyAPIView):
    queryset = Couturier.objects.all()
    serializer_class = CouturierSerializer
    lookup_field = 'id'  # Utiliser l'ID du Couturier pour les opérations