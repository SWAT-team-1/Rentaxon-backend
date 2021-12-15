from rest_framework import serializers
from .models import NewUser


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"
        extra_kwargs = {"password":{'write_only': True}}

        def create(self,validated_data):
            user = NewUser.objects.create(validated_data['phone'],None,validated_data['password'])
            return user


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"
        extra_kwargs = {'password':{'write_only': True}}