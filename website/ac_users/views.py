from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins, status
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer, RegisterSerializer



class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer: RegisterSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user: User = serializer.create(
            validated_data=serializer.validated_data
        )
        # if serializer.validated_data.get('role') == 'teacher':
        #     teacher: Teachers = serializer.create_teacher(
        #         validated_data=serializer.validated_data, user=user
        #     )

        refresh = CustomTokenObtainPairSerializer.get_token(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


# class CustomUserAPIList(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#
# class CustomUserAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = (IsAuthenticated, )
#     # authentication_classes = (TokenAuthentication, )
#
#
# class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     # permission_classes = (IsAdminOrReadOnly, )
#
#
# class CreateUserAPI(CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = (IsAuthenticated, )
#     # authentication_classes = (TokenAuthentication, )


# class CreateUserAPI(CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     # permission_classes = (AllowAny,)
#
#
# class UpdateUserAPI(UpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer



