from django_filters import rest_framework as filters

from .models import Abnormal


class AbnormalFilter(filters.FilterSet):
    user = filters.CharFilter(field_name="user_id__username", lookup_expr="icontains")

    class Meta:
        model = Abnormal
        fields = ["user"]
