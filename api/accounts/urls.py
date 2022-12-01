from django.urls import path

from .views import (
    UserRegisterAPIView, EmailVerifyAPIView,
    UserLoginAPIView, UserProfileAPIView
)

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('email/verify/', EmailVerifyAPIView.as_view(), name='email-verify'),
    path('profile/<int:pk>/', UserProfileAPIView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'post': 'create'
    }), name='profile')
]