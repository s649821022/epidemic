from django_filters import rest_framework as filters

from .models import Notices


class NoticesFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Notices
        fields = ["title"]
