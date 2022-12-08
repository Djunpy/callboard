from django.shortcuts import get_object_or_404
from django.core.exceptions import EmptyResultSet
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Car, Bus, Motorbike
from .serializers import (
    ReadCarSerializer,
    ReadBusSerializer, ReadMotorbikeSerializer,
     ShortMotorbikeSerializer,

)
from advert.paginations import CommonListPagination
from advert.seralizers import ShortAdvertSerializer


class CarAPIView(ModelViewSet):
    pagination_class = CommonListPagination

    def get_queryset(self):
        queryset = Car.objects.filter(status='published')\
            .select_related('address', 'brand', 'body_type', 'type_brand', 'category')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortAdvertSerializer
        if self.action == 'retrieve':
            return ReadCarSerializer


class BusAPIView(ModelViewSet):
    pagination_class = CommonListPagination

    def get_queryset(self):
        queryset = Bus.objects.filter(status='published')\
            .select_related('address', 'brand', 'body_type', 'type_brand', 'category')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortAdvertSerializer
        if self.action == 'retrieve':
            return ReadBusSerializer


class MotorBikeAPIVIew(ModelViewSet):
    pagination_class = CommonListPagination

    def get_queryset(self):
        queryset = Motorbike.objects.filter(status='published')\
            .select_related('address', 'brand', 'type_brand', 'category')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortAdvertSerializer
        if self.action == 'retrieve':
            return ReadMotorbikeSerializer




