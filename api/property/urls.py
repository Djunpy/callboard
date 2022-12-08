from django.urls import path

from .views import FlatAPIView, HouseAPIView

app_name = 'property'


urlpatterns = [
    path('flat/', FlatAPIView.as_view({
        'get': 'list'
    }), name='flat-list'),
    path('flat/<int:pk>/', FlatAPIView.as_view({
        'get': 'retrieve'
    }), name='flat-detail'),
    path('house/', HouseAPIView.as_view({
        'get': 'list'
    }), name='house-list'),
    path('house/<int:pk>/', HouseAPIView.as_view({
        'get': 'retrieve'
    }), name='house-detail')
]