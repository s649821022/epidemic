from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import VaccinateFilter
from .models import Vaccinate
from .serializers import VaccinateCreateSerializer, VaccinateSerializer


class VaccinateViewSet(viewsets.ModelViewSet):
    filter_class = VaccinateFilter

    def get_queryset(self):
        queryset = Vaccinate.objects.all().order_by("-created_at")
        return queryset

    def get_permissions(self):
        if self.action in {"create", "partial_update"}:
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in {"retrieve", "list"}:
            return VaccinateSerializer
        elif self.action in {"create", "partial_update"}:
            return VaccinateCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
