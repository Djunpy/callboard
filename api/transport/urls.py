from django.urls import path

from .views import CarAPIView, BusAPIView, MotorBikeAPIVIew


app_name = 'transport'

urlpatterns = [
    path('car/', CarAPIView.as_view({
        'get': 'list',
    }), name='car-list'),
    path('car/<int:pk>/', CarAPIView.as_view({
        'get': 'retrieve',
    }), name='car-detail'),
    path('bus/', BusAPIView.as_view({
        'get': 'list',
    }), name='bus-list'),
    path('bus/<int:pk>/', BusAPIView.as_view({
        'get': 'retrieve'
    }), name='bus-detail'),
    path('motorbike/', MotorBikeAPIVIew.as_view({
        'get': 'list'
    }), name='motorbike-list'),
    path('motorbike/<int:pk>/', MotorBikeAPIVIew.as_view({
        'get': 'retrieve'
    }), name='motorbike-detail')
]