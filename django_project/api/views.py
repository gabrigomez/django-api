from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('Working')

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
