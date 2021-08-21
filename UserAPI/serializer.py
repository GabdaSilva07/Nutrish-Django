from rest_framework import serializers
<<<<<<< HEAD
from .models import UserInfo

# Lead Serializer
class UserInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserInfo 
    fields = '__all__'
=======
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializer import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
>>>>>>> master
