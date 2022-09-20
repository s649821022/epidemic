from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import NoticesFilter
from .models import Notices
from .serializers import NoticesCreateSerializer, NoticesListSerializer


class NoticesViewSet(viewsets.ModelViewSet):
    filter_class = NoticesFilter

    def get_queryset(self):
        queryset = Notices.objects.all().order_by("-created_at")
        return queryset

    def get_permissions(self):
        if self.action in {"create", "partial_update"}:
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in {"retrieve", "list"}:
            return NoticesListSerializer
        elif self.action in {"create", "partial_update"}:
            return NoticesCreateSerializer
