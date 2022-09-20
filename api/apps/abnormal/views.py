from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import AbnormalFilter
from .models import Abnormal
from .serializers import AbnormalCreateSerializer, AbnormalSerializer


class AbnormalViewSet(viewsets.ModelViewSet):
    filter_class = AbnormalFilter

    def get_queryset(self):
        queryset = Abnormal.objects.all().order_by("-created_at")
        return queryset

    def get_permissions(self):
        if self.action in {"create", "partial_update"}:
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in {"retrieve", "list"}:
            return AbnormalSerializer
        elif self.action in {"create", "partial_update"}:
            return AbnormalCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
