from django_filters import rest_framework as filters

from .models import Vaccinate


class VaccinateFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    card = filters.CharFilter(field_name="card", lookup_expr="icontains")
    phone = filters.CharFilter(field_name="phone", lookup_expr="icontains")
    address = filters.CharFilter(field_name="address", lookup_expr="icontains")

    class Meta:
        model = Vaccinate
        fields = ["name", "card", "phone", "address"]
