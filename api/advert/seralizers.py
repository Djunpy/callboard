from rest_framework import serializers

from address.serializers import ReadAddressSerializer
from .models import Picture, Discount


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class ShortAdvertSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    published = serializers.ReadOnlyField()
    address = ReadAddressSerializer()

    class Meta:
        fields = ('id', 'name', 'published', 'address')




