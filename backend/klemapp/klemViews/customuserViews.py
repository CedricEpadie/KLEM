from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from klemapp.models import CustomUser, Client, Couturier
from klemapp.klemSerializer import CustomUserSerializer, RegisterSerializer, LoginSerializer, LogoutSerializer
from django.contrib.auth import logout, authenticate, login

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'patch']

class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user.is_couturier:
                Couturier.objects.create(user=user)
                return Response({'message': 'Couturier register succefully'}, status=status.HTTP_201_CREATED)
            else:
                Client.objects.create(user=user)
                return Response({'message': 'Client register succefulle'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post', 'patch']
    
    def create(self, request,  *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            
            if user is not None:
                login(request, user)
                if user.is_couturier:
                    return Response(
                        {
                            'message': 'Utilisateur connecté',
                            'url': 'vers la vue couturier'
                        },
                        status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {
                            'message': 'Utilisateur connecté',
                            'url': 'vers le vue client'
                        },
                        status=status.HTTP_200_OK
                    )
            else:
                return Response(
                    {'error': 'Email ou mot de passe incorrect'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        
    
class LogoutViewSet(viewsets.ModelViewSet):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        try:
            logout(request)
            return Response(
                    {
                        'message': 'Deconnexion reussie',
                        'url': 'vers la vue de connexion'
                    }, 
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {'error': 'une erreur s\'est produite lors de la déconnexion'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )