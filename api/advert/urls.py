from django.urls import path

from .views import ShortAdvertAPIView, AdvertSearchAPIVIew


app_name = 'advert'


urlpatterns = [
    # path('short/', ShortAdvertAPIView.as_view(), name='short-advert'),
    path('search/', AdvertSearchAPIVIew.as_view({
        'get': 'list',
    }), name='search'),
]