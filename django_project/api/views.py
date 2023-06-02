from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, CreateUserSerializer
from .models import User
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
def main(request):
    return HttpResponse('Working')

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = make_password(serializer.data.get('password'))
            username = serializer.data.get('username')
            
            user = User(email=email, password=password, username=username)
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class UserDetailsView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get(self, request, id):
        try:
            user = User.objects.get(id_user=id)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            user = None
            return Response({"Usuário não existe"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id):
        try:
            user = User.objects.get(id_user=id)
            user.delete()
            return Response({'Usuário excluído com sucesso'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            user = None
            return Response({"Usuário não existe"}, status=status.HTTP_404_NOT_FOUND)
            
    def put(self, request, id):
        try:
            user = User.objects.get(id_user=id)

            serializer = UserSerializer(user, data=request.data)        
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({"Erro na requisição"},status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"Usuário não encontrado"},status=status.HTTP_404_NOT_FOUND)



