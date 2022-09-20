from notices.models import Notices
from rest_framework import serializers


class NoticesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = ["id", "created_at", "modified_at", "title", "detail"]


class NoticesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = ["id", "title", "detail"]
