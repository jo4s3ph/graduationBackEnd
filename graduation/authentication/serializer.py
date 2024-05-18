import json
from dataclasses import field
from faculty_member.models import FacultyMemberProfile
from student.models import StudentProfile
from system_admin.models import SystemAdminProfile
from .models import OneTimePassword, User
from rest_framework import serializers
from string import ascii_lowercase, ascii_uppercase
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import send_normal_email
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class VerifyUserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneTimePassword
        fields = ['otp']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'role', 'edu_id', 'password', 'password2']

    def validate(self, attrs):
        # Ensure the two passwords match
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        # Create a new user and corresponding profile based on role
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            edu_id=validated_data.get('edu_id'),
            role=validated_data.get('role'),
            password=validated_data.get('password')
        )
        role = validated_data.get('role')
        if role == 'A':
            SystemAdminProfile.objects.create(user=user)
        elif role == 'F':
            FacultyMemberProfile.objects.create(user=user)
        elif role == 'S':
            StudentProfile.objects.create(user=user)

        return user


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, write_only=True)
    full_name = serializers.CharField(max_length=255, read_only=True)
    edu_id = serializers.CharField(max_length=255, read_only=True)
    role = serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'access_token', 'role', 'edu_id', 'refresh_token']

    def validate(self, attrs):
        # Authenticate user and generate JWT tokens
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)

        # print(f"{attrs.get('email')} and {email}")
        # print(f"{attrs.get('password')} and {password}")
        # print(f"{self.context.get('request')}********** {request}")
        

        if not user:
            raise AuthenticationFailed("Invalid credentials, try again.")  # User not found or incorrect password

        if not user.is_verified:
            raise AuthenticationFailed("Email is not verified")  # Email not verified

        tokens = user.tokens()
        return {
            'email': user.email,
            'full_name': user.get_full_name,
            "access_token": str(tokens.get('access')),
            "refresh_token": str(tokens.get('refresh')),
            'role': user.role,
            'edu_id': user.edu_id,
        }




class LogoutUserSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        # Validate the refresh token
        self.token = attrs.get('refresh_token')
        return attrs

    def save(self, **kwargs):
        # Blacklist the refresh token to log out the user
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            return self.fail('bad_token')
