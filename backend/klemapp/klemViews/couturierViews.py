from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from klemapp.models import Couturier, CustomUser
from klemapp.klemSerializer import CouturierSerializer

class CouturierViewSet(viewsets.ModelViewSet):
    queryset = Couturier.objects.all()
    serializer_class = CouturierSerializer
    
    def destroy(self, request, *args, **kwargs):
        couturier = self.get_object()
        customuser = CustomUser.objects.get(username = couturier.user.username)
        couturier.delete()
        customuser.delete()
        
        return Response(
            {'Message': 'Couturier supprilé avec succes'},
            status=status.HTTP_204_NO_CONTENT
        )