from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import UserListApiView, UserCreateApiView, UserRetrieveApiView, UserUpdateApiView, UserDestroyApiView, \
    UserTokenObtainPairView


app_name = UsersConfig.name
urlpatterns = [
    # User urlpatterns
    path('', UserListApiView.as_view(), name='users_list'),
    path('create/', never_cache(UserCreateApiView.as_view()), name='user_create'),
    path('<int:pk>/', UserRetrieveApiView.as_view(), name='user_detail'),
    path('<int:pk>/update/', never_cache(UserUpdateApiView.as_view()), name='user_update'),
    path('<int:pk>/delete/', never_cache(UserDestroyApiView.as_view()), name='user_delete'),

    # Token urlpatterns
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]