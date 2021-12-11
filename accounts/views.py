from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import NewUserSerializer
from .models import NewUser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from rest_framework import status


class UserList(ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    
    
class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    