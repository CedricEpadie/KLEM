from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from klemapp.models import Client, CustomUser
from klemapp.klemSerializer import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def destroy(self, request, *args, **kwargs):
        client = self.get_object()
        customuser = CustomUser.objects.get(username = client.user.username)
        client.delete()
        customuser.delete()
        
        return Response(
            {'message': 'Client supprimé avec succes'},
            status=status.HTTP_204_NO_CONTENT
        )