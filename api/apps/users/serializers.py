from django.contrib.auth import get_user_model
from djoser.serializers import (
    SetPasswordRetypeSerializer,
    UserCreatePasswordRetypeSerializer,
)
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegisterSerializer(UserCreatePasswordRetypeSerializer):
    email = serializers.EmailField()


class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.ImageField(source="avatar_thumbnail")

    class Meta:
        model = User
        fields = ["id", "username", "level", "avatar_url", "email", "last_login", "is_superuser"]
        read_only_fields = ["id", "level", "username", "last_login", "is_superuser"]


class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = self.user.username
        data["is_superuser"] = self.user.is_superuser
        return data


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class PasswordSerializer(SetPasswordRetypeSerializer):
    def set_password(self):
        new_password = self.validated_data["new_password"]
        user = self.context["request"].user
        print(user)
        user.set_password(new_password)
        user.save()
