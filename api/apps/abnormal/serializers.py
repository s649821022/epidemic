from abnormal.models import Abnormal
from rest_framework import serializers
from users.serializers import UserSerializer


class AbnormalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Abnormal
        fields = [
            "id",
            "user",
            "detail",
            "created_at",
            "modified_at",
        ]


class AbnormalCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Abnormal
        fields = [
            "id",
            "detail",
            "user",
        ]
