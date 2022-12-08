from django.shortcuts import render, get_object_or_404
import jwt
import os
from itertools import chain
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
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from .seralizers import ShortAdvertSerializer
from transport.models import Car, Motorbike, Bus, OtherTransport
from .paginations import CommonListPagination

class ShortAdvertAPIView(ListModelMixin, GenericViewSet):
    serializer_class_car = ShortAdvertSerializer

    def get_queryset_car(self):
        query = Car.objects.only('id', 'name', 'address')

        return query

    # def list(self, request, *args, **kwargs):
    #     car = self.serializer_class_car(self.get_queryset_car(), many=True).data
    #
    #     data = {
    #         'msg': 'Success',
    #         'car': car
    #     }
    #     return Response(data, status=status.HTTP_200_OK)



class AdvertSearchAPIVIew(ListModelMixin, GenericViewSet):
    serializer_class = ShortAdvertSerializer
    pagination_class = CommonListPagination

    def get_queryset(self):
        query = self.request.GET.get('q', None)

        if query is not None:
            car = Car.search_object.search(query)
            motorbike = Motorbike.search_object.search(query)
            bus = Bus.search_object.search(query)

            queryset_chain = chain(
                car, motorbike, bus
            )
            qs = sorted(
                queryset_chain,
                key=lambda instance: instance.pk, reverse=True
            )
            return qs


















