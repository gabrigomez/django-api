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
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class FindeUserView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.data.get('id_user')
            user = User(id_user=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

