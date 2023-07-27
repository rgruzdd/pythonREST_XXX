from django.contrib import admin
from django.contrib.admin import site
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ac_users.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include("ac_users.urls")),
    # path('api/', include("students.urls")),
    # path('api/', include("teachers.urls")),
    path('api/', include("web_details.urls")),
    # path('create-user/', CreateUserAPI.as_view()),
]


#     path('', include(router.urls)),
#     path('register/', UserRegistrationView.as_view(), name='user_register'),
#     path('login/', UserLoginView.as_view(), name='user_login'),
#     # path('create-user/', views.CreateUserAPI.as_view()),
#     # path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
#     # path('login/', views.LoginAPIView.as_view()),
#     # path('logout/', LogoutView.as_view()),

