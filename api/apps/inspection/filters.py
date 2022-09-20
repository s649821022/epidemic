from django_filters import rest_framework as filters

from .models import Inspection


class InspectionFilter(filters.FilterSet):
    location = filters.CharFilter(field_name="location", lookup_expr="icontains")
    result = filters.CharFilter(field_name="result", lookup_expr="icontains")

    class Meta:
        model = Inspection
        fields = ["location", "result"]
