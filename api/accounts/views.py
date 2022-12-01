import jwt
import os
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserLoginSerializer, UserRegisterSerializer,
    UserChangePasswordSerializer, UserProfileSerializer,
    UserSerializer
)

from .permissions import IsCurrentUserOwnerOrReadOnly
from .tasks import sender_token_verify_email
from .models import Profile

User = get_user_model()


class UserRegisterAPIView(GenericAPIView):

    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            data = {
                'msg': 'Confirm your registration by entering the code sent to your email',
                'user_id': user.pk
            }
            current_site = get_current_site(request=request).domain
            sender_token_verify_email(user.pk, current_site)
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_id = request.GET.get('user_id', '')
        try:
            user = User.objects.get(pk=user_id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is None:
            return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
        current_site = get_current_site(request=request).domain
        sender_token_verify_email(user.id, current_site)
        return Response('The letter was sent again', status=status.HTTP_200_OK)


class EmailVerifyAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get('token', '')
        try:
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('JWT_ALGORITHM')])
            user = User.objects.get(pk=payload['user_id'])
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is None:
            return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
        user.is_email_verify = True
        user.save()
        return Response('Email successfully confirmed', status=status.HTTP_200_OK)


class UserLoginAPIView(GenericAPIView):

    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        context = {
            'request': request
        }
        serializer = self.get_serializer(data=request.data, context=context)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            token = RefreshToken.for_user(user)
            data = {
                'msg': 'Login has been successfully',
                'user': UserSerializer(user, context=self.get_serializer_context()).data,
                'token': {
                    'refresh': str(token),
                    'access': str(token.access_token)
                }
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [IsCurrentUserOwnerOrReadOnly]
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





