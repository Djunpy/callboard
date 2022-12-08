from rest_framework import serializers

from .models import House, Flat, Plot

from address.serializers import ReadAddressSerializer


class ReadFlatSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    address = ReadAddressSerializer()
    contact = serializers.CharField(source='get_contact_display')
    repair = serializers.CharField(source='get_repair_display')
    house_type = serializers.CharField(source='get_house_type_display')
    parking = serializers.CharField(source='get_parking_display')
    housing_stock = serializers.CharField(source='get_housing_stock_display')
    bathroom = serializers.CharField(source='get_bathroom_display')
    type_offer = serializers.CharField(source='get_type_offer_display')

    class Meta:
        model = Flat
        fields = (
            'id', 'user', 'contact', 'name', 'address',
            'description', 'pictures', 'category',
            'published', 'repair', 'floor_in_house',
            'tv', 'internet', 'floor', 'house_type',
            'parking', 'housing_stock', 'balcony',
            'loggia', 'bathroom', 'furniture_kitchen',
            'furniture_clothes_places', 'furniture_sleeping_places',
            'washing_machine', 'dishwasher', 'total_area', 'living_space',
            'number_of_rooms', 'ceiling_height', 'type_offer',
            'conditioner', 'fridge', 'elevator'
        )


class ReadHouseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    address = ReadAddressSerializer()
    contact = serializers.CharField(source='get_contact_display')
    repair = serializers.CharField(source='get_repair_display')
    parking = serializers.CharField(source='get_parking_display')
    type_house = serializers.CharField(source='get_type_house_display')
    wall_material = serializers.CharField(source='get_wall_material_display')

    class Meta:
        model = House
        fields = (
            'id', 'user', 'contact', 'name',
            'description', 'pictures', 'category',
            'published', 'repair', 'floor_in_house',
            'tv', 'internet', 'parking', 'type_house',
            'wall_material', 'bath', 'poll', 'year_of_construction',
            'number_of_rooms', 'house_area', 'land_area', 'bathroom_street',
            'bathroom_house', 'asphalt_road', 'public_transport', 'pharmacy',
            'shop', 'kindergarten'
        )


class ReadPlotSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    address = ReadAddressSerializer()
    contact = serializers.CharField(source='get_contact_display')
    type_plot = serializers.CharField(source='get_type_plot_display')

    class Meta:
        model = Plot
        fields = (
            'id', 'user', 'contact', 'name',
            'description', 'pictures', 'category',
            'published', 'type_plot', 'land_area',
            'gas', 'water_supply', 'sewerage',
            'power_supply'
        )