import time
import requests
from django.contrib.auth import authenticate
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from .models import User
from .serializers import UserSerializer

class SignupView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'token': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SigninView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        id = request.data.get('id')
        password = request.data.get('password')
        user = authenticate(id=id, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class InfoView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'id': user.id, 'id_type': user.id_type}, status=status.HTTP_200_OK)

class LatencyView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start = time.time()
        requests.get("https://ya.ru")
        latency = time.time() - start
        return Response({'latency': latency}, status=status.HTTP_200_OK)

class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        all_logout = request.data.get('all', False)
        if all_logout:
            RefreshToken.for_user(request.user).blacklist()
        return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)
