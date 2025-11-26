from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from apps.users.serializers import UserSerializer


# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
