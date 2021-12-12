from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token["email"] = user.user_email
        token["username"] = user.user_name
        token["phone_number"] = user.phone_number
        token["address"] = user.address
        token["avatar"] = user.avatar
        return token

class MyTokenObtainPairCustomView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer