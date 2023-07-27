from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from django.urls import path, include

from .views import *


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='user_login'),
    # path('create-user/', views.CreateUserAPI.as_view()),
    # path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    # path('login/', views.LoginAPIView.as_view()),
    # path('logout/', LogoutView.as_view()),
]