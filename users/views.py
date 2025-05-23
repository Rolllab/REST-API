from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,AllowAny

from users.models import User
from users.serializers.user_serializers import (UserSerializer, UserCreateSerializer, UserUpdateSerializer,
                                                UserTokenObtainPairSerializer)



class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (IsAuthenticated, )


class UserRetrieveApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )


class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     return User.objects.filter(id=user.id)


class UserDestroyApiView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer