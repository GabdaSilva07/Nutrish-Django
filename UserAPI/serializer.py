from django.db.models import fields
from django.urls.conf import include
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# from .serializer import User
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # extra_kwargs = {'password': {'write_only': True, 'required': True}}
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "password"]
#         extra_kwargs = {'password': {'write_only': True, 'required': True}}
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user