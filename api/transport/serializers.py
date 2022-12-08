from rest_framework import serializers

from .models import Car, Bus, Motorbike, OtherTransport, TransportBodyType
from advert.seralizers import PictureSerializer, DiscountSerializer
from advert.models import AdvertCategory, Picture, Discount
from address.serializers import ReadAddressSerializer
from address.models import Address


# class ChoiceField(serializers.ChoiceField):
#
#     def to_representation(self, obj):
#         if obj == '' and self.allow_blank:
#             return obj
#         return self._choices[obj]
#
#     def to_internal_value(self, data):
#         # To support inserts with the value
#         if data == '' and self.allow_blank:
#             return ''
#
#         for key, val in self._choices.items():
#             if val == data:
#                 return key
#         self.fail('invalid_choice', input=data)




class ShortMotorbikeSerializer(serializers.ModelSerializer):
    address = ReadAddressSerializer()
    class Meta:
        model = Motorbike
        fields = ('id', 'name', 'address')

    @classmethod
    def setup_eager_loading(cls, queryset):
        queryset = queryset.only(*cls.Meta.fields)
        return queryset


class ReadCarSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    address = ReadAddressSerializer()
    contact = serializers.CharField(source='get_contact_display')
    color = serializers.CharField(source='get_color_display')
    condition = serializers.CharField(source='get_condition_display')
    condition_2 = serializers.CharField(source='get_condition_2_display')
    salom = serializers.CharField(source='get_salom_display')
    power_steering = serializers.CharField(source='get_power_steering_display')
    climat_control = serializers.CharField(source='get_climat_control_display')
    power_windows = serializers.CharField(source='get_power_windows_display')
    type_engine = serializers.CharField(source='get_type_engine_display')
    type_transmission = serializers.CharField(source='get_type_transmission_display')
    drive_unit = serializers.CharField(source='get_drive_unit_display')
    audio_system = serializers.CharField(source='get_audio_system_display')
    headlights = serializers.CharField(source='get_headlights_display')
    category = serializers.ReadOnlyField(source='category.name')
    brand = serializers.ReadOnlyField(source='brand.name')
    type_brand = serializers.ReadOnlyField(source='type_brand.name')
    body_type = serializers.ReadOnlyField(source='body_type.name')
    pictures = PictureSerializer(many=True)

    class Meta:
        model = Car
        fields = (
           'id', 'user', 'contact', 'name',
            'description', 'pictures', 'category',
            'published', 'brand', 'type_brand',
            'color', 'discount', 'condition',
            'condition_2', 'mileage', 'owners',
            'cd_dvd', 'mp3', 'radio', 'video',
            'usb', 'aux', 'bluetooth', 'gps',
            'automatic_valet', 'rain_sensor',
            'light_sensor', 'front_parking_sensors',
            'rear_parking_sensors', 'blind_spot_monitor',
            'rear_view_camera', 'cruise_control',
            'on_board_computer', 'signaling',
            'central_locking', 'satellite',
            'immobilizer', 'frontal', 'knees',
            'curtains', 'side_front', 'side_rear',
            'anti_lock_brakes', 'anti_slip',
            'exchange_rate_stability', 'decay_of_braking_forces',
            'emergency_braking', 'differential_block',
            'pedestrian_detection', 'front_seats',
            'rear_seats', 'mirror', 'steering_columns',
            'front_seats', 'rear_seats', 'mirror', 'steering_column',
            'folding_mirrors', 'salom', 'power_steering',
            'climat_control', 'steering_wheel_control',
            'athermal_glazing', 'power_windows', 'type_engine',
            'engine_volume', 'power', 'type_transmission',
            'drive_unit', 'fuel_consumption_mixed',
            'acceleration_to', 'audio_system', 'subwoofer',
            'headlights', 'fog', 'headlight_washers',
            'adaptive_lighting', 'tires_and_wheels',
            'winter_tires', 'front_seats', 'rear_seats',
            'mirrors', 'rear_glass', 'rudder', 'body_type',
            'address'
        )


class ReadBusSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    address = ReadAddressSerializer()
    contact = serializers.CharField(source='get_contact_display')
    pictures = PictureSerializer(many=True)
    brand = serializers.ReadOnlyField(source='brand.name')
    type_brand = serializers.ReadOnlyField(source='type_brand.name')
    body_type = serializers.ReadOnlyField(source='body_type.name')
    color = serializers.CharField(source='get_color_display')
    condition = serializers.CharField(source='get_condition_display')
    condition_2 = serializers.CharField(source='get_condition_2_display')
    class Meta:
        model = Bus
        fields = (
            'user', 'address', 'contact',
            'address', 'pictures', 'brand',
            'type_brand', 'body_type', 'color', 'discount',
            'condition', 'condition_2', 'mileage',
            'owners', 'description', 'name'
        )


class ReadMotorbikeSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    address = ReadAddressSerializer()
    contact = serializers.CharField(source='get_contact_display')
    pictures = PictureSerializer(many=True)
    color = serializers.CharField(source='get_color_display')
    condition = serializers.CharField(source='get_condition_display')
    condition_2 = serializers.CharField(source='get_condition_2_display')
    type_engine = serializers.CharField(source='get_type_engine_display')
    fuel_supply = serializers.CharField(source='get_fuel_supply_display')
    type_of_drive = serializers.CharField(source='get_type_of_drive_display')
    type_transmission = serializers.CharField(source='get_type_transmission_display')
    cylinder_arrangement = serializers.CharField(source='get_cylinder_arrangement_display')
    cooling = serializers.CharField(source='get_cooling_display')

    class Meta:
        model = Motorbike
        fields = (
            'user', 'address', 'contact',
            'address', 'pictures', 'brand',
            'type_brand', 'color', 'discount',
            'condition', 'condition_2', 'mileage',
            'owners', 'type_engine', 'type_of_drive',
            'type_transmission', 'cylinder_arrangement',
            'cooling', 'fuel_supply', 'electric_starter',
            'abs', 'tcs', 'start_stop_sys', 'windshield',
            'cofr', 'Number_of_cycles', 'number_of_cylinders',
            'description', 'name'
        )


class ReadOtherTransportSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    address = ReadAddressSerializer()
    contact = serializers.CharField(source='get_contact_display')
    brand = serializers.ReadOnlyField(source='brand.name')
    type_brand = serializers.ReadOnlyField(source='type_brand.name')
    pictures = PictureSerializer(many=True)
    color = serializers.CharField(source='get_color_display')
    condition = serializers.CharField(source='get_condition_display')
    condition_2 = serializers.CharField(source='get_condition_2_display')

    class Meta:
        model = OtherTransport
        fields = (
            'user', 'address', 'contact',
            'address', 'pictures', 'brand',
            'type_brand', 'color' 'discount',
            'description', 'name'
        )























# class CarSerializer(serializers.ModelSerializer):
#     body_type = serializers.SlugRelatedField(queryset=TransportBodyType.objects.all(), slug_field='name')
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     pictures = PictureSerializer(partial=True, required=False)
#     address = AddressSerializer(partial=True, required=False)
#     discount = DiscountSerializer(partial=True, required=False)
#     class Meta:
#         model = Car
#         fields = (
#             'user', 'contact', 'pictures', 'category', 'status',
#             'published', 'address', 'condition', 'price',  'discount',
#             'condition', 'condition_2', 'mileage', 'owners',
#             'cd_dvd', 'mp3', 'radio', 'video', 'usb', 'aux',
#             'bluetooth', 'gps', 'automatic_valet', 'rain_sensor',
#             'light_sensor', 'front_parking_sensors', 'rear_parking_sensors',
#             'blind_spot_monitor', 'rear_view_camera', 'cruise_control', 'on_board_computer',
#             'signaling', 'central_locking', 'satellite', 'immobilizer',
#             'frontal', 'knees', 'curtains', 'side_front', 'side_rear',
#             'anti_lock_brakes', 'anti_slip', 'exchange_rate_stability',
#             'decay_of_braking_forces', 'emergency_braking', 'differential_block',
#             'pedestrian_detection', 'front_seats', 'rear_seats', 'mirrors',
#             'rear_glass', 'rudder', 'front_seats', 'rear_seats', 'mirror',
#             'steering_column', 'folding_mirrors', 'front_seats', 'rear_seats',
#             'mirror', 'steering_columns', 'salom', 'power_steering', 'climat_control',
#             'steering_wheel_control', 'athermal_glazing', 'power_windows',
#             'type_engine', 'engine_volume', 'power', 'type_transmission', 'drive_unit',
#             'fuel_consumption_mixed', 'acceleration_to', 'audio_system', 'subwoofer',
#             'headlights', 'fog', 'headlight_washers', 'adaptive_lighting', 'tires_and_wheels',
#             'winter_tires', 'body_type',
#         )
#
#
#     def get_or_create_pictures(self, pictures):
#         picture_ids = []
#         for picture in pictures:
#             instance_picture, created = Picture.objects.get_or_create(**picture)
#             picture_ids.append(instance_picture.pk)
#         return picture_ids
#     def create(self, validated_data):
#         pictures = validated_data.pop('pictures', [])
#         address = validated_data.pop('address', [])
#         discount = validated_data.pop('discount', [])
#         instance_address = Address.objects.create(**address)
#         instance_discount = Discount.objects.create(**discount)
#         car = Car.objects.create(**validated_data)
#         car.pictures.set(self.get_or_create_pictures(pictures))
#         car.address = instance_address
#         car.discount = instance_discount
#         car.save()
#         return car
#

