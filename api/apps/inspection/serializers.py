from inspection.models import Inspection
from rest_framework import serializers
from users.serializers import UserSerializer


class InspectionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Inspection
        fields = [
            "id",
            "location",
            "result",
            "detail",
            "user",
            "created_at",
            "modified_at",
        ]


class InspectionCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Inspection
        fields = ["id", "location", "result", "detail", "user"]
