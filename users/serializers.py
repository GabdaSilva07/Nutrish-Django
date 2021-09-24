from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password', 'diet', 'intolerance', 'favourite1', 'favourite2', 'favourite3', 'favourite4', 'favourite5')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'diet', 'intolerance', 'favourite1', 'favourite2', 'favourite3', 'favourite4', 'favourite5')