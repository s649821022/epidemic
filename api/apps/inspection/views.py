from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import InspectionFilter
from .models import Inspection
from .serializers import InspectionCreateSerializer, InspectionSerializer


class InspectionViewSet(viewsets.ModelViewSet):
    filter_class = InspectionFilter

    def get_queryset(self):
        queryset = Inspection.objects.all().order_by("-created_at")
        return queryset

    def get_permissions(self):
        if self.action in {"create", "partial_update"}:
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in {"retrieve", "list"}:
            return InspectionSerializer
        elif self.action in {"create", "partial_update"}:
            return InspectionCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
