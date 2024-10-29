from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Client, Couturier
from .klemSerializer import CustomUserSerializer
from django.contrib.auth import login, logout

class InscriptionAPI(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            if CustomUser.objects.filter(username=request.data.get('username')).exists():
                return Response(
                    {'error': 'username déjà utilisé'},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            if CustomUser.objects.filter(email=request.data.get('email')).exists():
                return Response(
                    {'error': 'email déjà utilisé'},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            user = serializer.save()
            if user.is_couturier:
                Couturier.objects.create(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                Client.objects.create(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConnexionAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = CustomUser.objects.get(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_couturier:
                return Response({'redirect': 'couturier'}, status=status.HTTP_200_OK)
            else:
                return Response({'redirect': 'client'}, status=status.HTTP_200_OK)
        return Response({'error': 'username or password was wrong!'}, status=status.HTTP_401_UNAUTHORIZED)

class DeconnexionAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'redirect': 'connexion'}, status=status.HTTP_200_OK)