from rest_framework import serializers
from users.serializers import UserSerializer
from vaccinate.models import Vaccinate


class VaccinateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Vaccinate
        fields = [
            "id",
            "name",
            "card",
            "phone",
            "address",
            "user",
            "vaccinateNo",
            "vaccinateTime",
            "created_at",
            "modified_at",
        ]


class VaccinateCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Vaccinate
        fields = [
            "id",
            "name",
            "card",
            "phone",
            "address",
            "user",
            "vaccinateNo",
            "vaccinateTime",
        ]
