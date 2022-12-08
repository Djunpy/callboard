from rest_framework import serializers

from .models import Address


class ReadAddressSerializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.name')
    city = serializers.ReadOnlyField(source='city.name')
    class Meta:
        model = Address
        fields = (
            'country', 'city', 'street',
            'house_number', 'apartment_number'
        )

