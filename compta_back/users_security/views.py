from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from users_security.serializers import LoginSerializer, RegisterSerializer
from users_security.models import User

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        LoginSerializer(request.data)
        try:
            user = User.objects.get(username=request.data['username'])
            if user.check_password(request.data['password']):
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Identifiants invalides'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'Cette utilisateur n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Utilisateur enregistré avec succès'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RefreshView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error': 'refresh token required'}, status=status.HTTP_400_BAD_REQUEST)
            
            refresh = RefreshToken(refresh_token)
            return Response({'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Refresh Token invalid ou expiré'}, status=status.HTTP_401_UNAUTHORIZED)