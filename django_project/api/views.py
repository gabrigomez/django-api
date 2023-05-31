from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, CreateUserSerializer
from .models import User
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def main(request):
    return HttpResponse('Working')

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            username = serializer.data.get('username')
            
            user = User(email=email, password=password, username=username)
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
