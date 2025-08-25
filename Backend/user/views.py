from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# ------------------------------
# Frontend home view
# ------------------------------
def home(request):
    return render(request, 'user/index.html')


# ------------------------------
# Register API
# ------------------------------
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            token, created = Token.objects.get_or_create(user=new_user)
            return Response({
                "success": True,
                "message": "Registration successful! Welcome to the Club",
                "user": {
                    "id": new_user.id,
                    "username": new_user.username
                },
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({"message": "GET request received. This endpoint is for POST requests."})


# ------------------------------
# Login API
# ------------------------------
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "🚪 Login successful! Welcome!",
                "token": token.key
            })
        else:
            return Response({
                "message": "Access Denied! Invalid Credentials"
            }, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return Response({"message": "GET request received. This endpoint is for POST requests."})


# ------------------------------
# Dashboard API
# ------------------------------
class DashboardView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"🎉 Welcome to your dashboard, {request.user.username}! You are authenticated. 🎉"
        })
