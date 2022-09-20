from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .epidemic_data import get_epidemic_data, get_latest_infected_number, get_risk_area, get_epidemic_news
from .models import Reptile
from .serializers import ReptileListSerializer


class ReptileViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = None

    def get_queryset(self):
        queryset = Reptile.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == "init":
            return ReptileListSerializer
        return super().get_serializer_class()

    @extend_schema(summary="get_epidemic_news")
    @action(["GET"], detail=False, url_name="getNews", url_path="getNews")
    def getNews(self, request, *args, **kwargs):
        """
        拉取疫情新闻
        """
        data = get_epidemic_news()
        return Response(data=data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="init_epidemic_data",
        responses={201: ReptileListSerializer},
    )
    @action(
        ["POST"],
        detail=False,
        url_path="init",
        url_name="init",
        serializer_class=ReptileListSerializer,
    )
    def init(self, request, *args, **kwargs):
        """
        初始化疫情数据
        """
        Reptile.objects.all().delete()
        data = get_epidemic_data()
        Reptile.objects.create(**data)
        return Response(data=data, status=status.HTTP_201_CREATED)

    @extend_schema(summary="get_area_list")
    @action(
        ["GET"],
        detail=False,
        url_path="getArea",
        url_name="getArea",
    )
    def getArea(self, request, *args, **kwargs):
        """
        获取低中高风险地区数据
        """
        data = get_risk_area()
        return Response(data=data, status=status.HTTP_200_OK)

    @extend_schema(summary="get_latest_infected_number")
    @action(
        ["GET"],
        detail=False,
        url_path="getRiskNumber",
        url_name="getRiskNumber",
    )
    def getRiskNumber(self, request, *args, **kwargs):
        """
        获取最近30日的感染人数
        """
        data = get_latest_infected_number()
        return Response(data=data, status=status.HTTP_200_OK)
