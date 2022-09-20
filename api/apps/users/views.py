from django.contrib.auth import get_user_model
from django.utils.timezone import now
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from users import signals
from users.filters import UserFilter
from users.serializers import (
    PasswordSerializer,
    RegisterSerializer,
    TokenSerializer,
    UserInfoSerializer,
    UserSerializer,
)

User = get_user_model()
jwt_auth = JWTAuthentication()


class AuthViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    authentication_classes = []
    serializer_class = None
    permission_classes = [AllowAny]
    filter_class = UserFilter

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == "register":
            return RegisterSerializer
        elif self.action == "login":
            return TokenSerializer
        elif self.action == "userinfo":
            return UserInfoSerializer
        elif self.action == "retrieve":
            return UserSerializer
        elif self.action == "list":
            return UserSerializer
        elif self.action == "partial_update":
            return UserSerializer
        elif self.action == "change_password":
            return PasswordSerializer
        return super().get_serializer_class()

    @extend_schema(
        summary="Register",
        responses={201: UserSerializer},
    )
    @action(
        ["POST"],
        detail=False,
        url_path="register",
        url_name="register",
        serializer_class=RegisterSerializer,
    )
    def register(self, request):
        """用户注册"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_active = True
        user.save()
        signals.user_registered.send(sender=self.__class__, user=user, request=self.request)
        output_serializer = UserSerializer(instance=user, context={"request": request})
        return Response(
            data=output_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(summary="Login", request=TokenSerializer, responses={200: TokenRefreshSerializer})
    @action(
        ["POST"],
        detail=False,
        url_path="login",
        url_name="login",
        serializer_class=TokenSerializer,
    )
    def login(self, request):
        """用户登录"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.last_login = now()
        user.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Refresh_token",
        request=TokenRefreshSerializer,
    )
    @action(
        ["POST"],
        detail=False,
        url_name="refresh_token",
        url_path="refresh_token",
        serializer_class=TokenRefreshSerializer,
    )
    def refresh_token(self, request):
        """刷新token"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    @extend_schema(summary="Logout")
    @action(
        ["POST"],
        detail=False,
        url_name="logout",
        url_path="logout",
        authentication_classes=[JWTAuthentication],
        permission_classes=[IsAuthenticated],
    )
    def logout(self, request):
        """退出登录"""
        header = jwt_auth.get_header(request)
        token = jwt_auth.get_raw_token(header).decode()
        validated_token = jwt_auth.get_validated_token(token)
        jwt_auth.get_user(validated_token)
        return Response(status=status.HTTP_200_OK)

    @extend_schema(summary="UserInfo")
    @action(
        ["GET"],
        detail=False,
        url_path="userinfo",
        url_name="userinfo",
        authentication_classes=[JWTAuthentication],
        permission_classes=[IsAuthenticated],
    )
    def userinfo(self, request):
        """获取当前登录人的信息"""
        user = User.objects.get(username=request.user)
        output_serializer = UserInfoSerializer(user)
        return Response(status=status.HTTP_200_OK, data=output_serializer.data)

    @extend_schema(
        summary="change_password",
        request=PasswordSerializer,
    )
    @action(
        ["POST"],
        detail=False,
        url_name="change_password",
        url_path="change_password",
        authentication_classes=[JWTAuthentication],
        permission_classes=[IsAuthenticated],
    )
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_password()
        signals.user_password_changed.send(sender=request.user.__class__, request=request, user=request.user)
        return Response(status=status.HTTP_200_OK)
