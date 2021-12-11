from rest_framework import serializers
from .models import NewUser
from phonenumber_field.serializerfields import PhoneNumberField

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('user_email', 'user_name', 'password','phone_number','address','avatar')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class NewUserSerializer(serializers.ModelSerializer):
    # pet=OrderItemserializers(many=True,read_only=True)

    class Meta:
        fields = "all"
        model = NewUser
