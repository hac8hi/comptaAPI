from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.views.decorators.csrf import ensure_csrf_cookie

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.conf import settings

from auth.users_security.services.auth import get_tokens
from auth.users_security.serializers import RegisterSerializer


class LoginView(APIView):

    @permission_classes([AllowAny])
    def post(self, request):
        data = request.data
        response = Response()        
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"Invalid" : "Invalid username or password!!"},status=status.HTTP_404_NOT_FOUND)

        if not user.is_active:
            return Response({"No active" : "This account is not active!!"},status=status.HTTP_404_NOT_FOUND)

        tokens = get_tokens(user)
        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
            value = tokens.get('access'),
            expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_REFRESH_COOKIE'], 
            value = tokens.get('refresh'),
            expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        response.data = {
            "success" : True,
            "message": "Vous êtes connecté."
        }
        response.status_code = status.HTTP_200_OK
        return response

class RegisterView(APIView):

    REQUIRED_FIELDS = [
        "username",
        "email",
        "password"
    ]

    @permission_classes([IsAdminUser])
    def post(self, request):
        data = request.data

        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                "success": False,
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({
            "success": True,
            "message": "Utilisateur inscrit avec succès !",
            "data": serializer.validated_data
        }, status=status.HTTP_201_CREATED)

class RefreshView(APIView):

    @permission_classes([AllowAny])
    def post(self, request):

        response = Response()   
        serializer = TokenRefreshSerializer(data=request.COOKIES)

        if not serializer.is_valid():
            return Response({'error': 'Jeton invalide ou expiré'}, status=status.HTTP_401_UNAUTHORIZED)

        tokens = serializer.validated_data

        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
            value = tokens.get('access'),
            expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_REFRESH_COOKIE'], 
            value = tokens.get('refresh'),
            expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        response.data = {
            "success" : True,
            "message": "Jeton rafraichie."
        }
        response.status_code = status.HTTP_200_OK
        return response