from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path('create-user/', views.CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view())
]


# urlpatterns = [
#     path('all-profiles', UserProfileListCreateView.as_view(), name="all-profiles"),
#     path('profile/<int:pk>', UserProfileDetailView.as_view(), name="profile"),
# ]