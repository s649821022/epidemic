from reptile.models import Reptile
from rest_framework import serializers


class ReptileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reptile
        fields = [
            "currentConfirmedCount",
            "confirmedCount",
            "suspectedCount",
            "curedCount",
            "deadCount",
            "seriousCount",
            "suspectedIncr",
            "currentConfirmedIncr",
            "confirmedIncr",
            "curedIncr",
            "deadIncr",
            "seriousIncr",
            "yesterdayConfirmedCountIncr",
            "yesterdaySuspectedCountIncr",
            "highDangerCount",
            "midDangerCount",
            "created_at",
            "modified_at",
        ]
        read_only_fields = [
            "currentConfirmedCount",
            "confirmedCount",
            "suspectedCount",
            "curedCount",
            "deadCount",
            "seriousCount",
            "suspectedIncr",
            "currentConfirmedIncr",
            "confirmedIncr",
            "curedIncr",
            "deadIncr",
            "seriousIncr",
            "yesterdayConfirmedCountIncr",
            "yesterdaySuspectedCountIncr",
            "highDangerCount",
            "midDangerCount",
            "created_at",
            "modified_at",
        ]
