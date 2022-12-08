from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import House, Flat, Plot
from .serializers import ReadFlatSerializer, ReadHouseSerializer, ReadPlotSerializer
from advert.seralizers import ShortAdvertSerializer
from advert.paginations import CommonListPagination

class FlatAPIView(ModelViewSet):
    pagination_class = CommonListPagination

    def get_queryset(self):
        queryset = Flat.objects.filter(status='published') \
            .select_related('address', 'category')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortAdvertSerializer
        if self.action == 'retrieve':
            return ReadFlatSerializer


class HouseAPIView(ModelViewSet):
    pagination_class = CommonListPagination

    def get_queryset(self):
        queryset = Flat.objects.filter(status='published') \
            .select_related('address', 'category')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortAdvertSerializer
        if self.action == 'retrieve':
            return ReadHouseSerializer


class PlotAPIView(ModelViewSet):
    pagination_class = CommonListPagination

    def get_queryset(self):
        queryset = Flat.objects.filter(status='published') \
            .select_related('address', 'category')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortAdvertSerializer
        if self.action == 'retrieve':
            return ReadPlotSerializer
