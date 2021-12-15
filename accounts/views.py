from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  NewUserSerializer, CreateUserSerializer
from rest_framework.permissions import AllowAny
from .models import NewUser
from django.contrib.auth.hashers import make_password

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        print(request.data)
        data = request.data
        reg_serializer = CreateUserSerializer(data=data)
        if reg_serializer.is_valid():
            password = reg_serializer.validated_data.get('password')
            reg_serializer.validated_data['password']=make_password(password)
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListCreateAPIView):

    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer