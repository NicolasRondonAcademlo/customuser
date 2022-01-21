from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import CustomUser
from core.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class RegisterApiView(
    generics.GenericAPIView
):
    serializer_class = CustomUserSerializer
    def post(self, request):
       serializer = self.serializer_class(
           data=request.data
       )
       if serializer.is_valid():
           serializer.save()
           return Response(
               data=serializer.data,
               status=status.HTTP_200_OK
           )
       return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class RegisterUserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin

):
    serializer_class = CustomUserSerializer
    model = CustomUser
    queryset = CustomUser.objects.all()