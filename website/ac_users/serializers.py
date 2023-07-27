from django.contrib.auth.password_validation import validate_password
from django.db import models
from django.db.models import CharField, EmailField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token['name'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        return token


class RegisterSerializer(ModelSerializer):
    email = EmailField(blank=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = CharField(blank=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password',  'email', 'role')

    def create(self, validated_data):
        user: User = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            role = validated_data.get('role'),
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user

    # def create_teacher(self, validated_data, user: User):
    #     teacher: Teachers = Teachers.objects.create(
    #         first_name=validated_data.get('first_name'),
    #         last_name=validated_data.get('last_name'),
    #         email=validated_data.get('email'),
    #         username=validated_data.get('username'),
    #         user_id=user.id
    #     )
    #
    #     teacher.save()
    #
    #     return teacher



