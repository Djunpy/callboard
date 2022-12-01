from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Profile
from address.models import Address
from address.serializers import AddressSerializer


User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.ReadOnlyField(source='user.username')
    address = AddressSerializer(partial=True)

    class Meta:
        model = Profile
        fields = (
            'photo', 'address',
            'username', 'user',
            'telegram_url',
            'facebook_url'
        )

    def create(self, validated_data):
        address = validated_data.pop('address')
        address = Address.objects.create(**address)
        profile = Profile.objects.create(**validated_data, address=address)
        return profile

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address
        instance.photo = validated_data.get('photo', instance.photo)
        instance.telegram_url = validated_data.get('telegram_url', instance.telegram_url)
        instance.facebook_url = validated_data.get('facebook_url', instance.facebook_url)
        address.city = address_data.get('city', address.city)
        address.country = address_data.get('country', address.country)
        address.house_number = address_data.get('house_number', address.house_number)
        address.apartment_number = address_data.get('apartment_number', address.apartment_number)
        address.save()
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username', 'email',
            'is_email_verify',
        )


class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'username', 'email', 'password',
            'password2'
        )

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ('password', 'username')

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            login(self.context['request'], user)
            user = User.objects.get(Q(username=user.username) | Q(username=user.email))
            return user
        raise serializers.ValidationError('Incorrect Credentials')


class UserChangePasswordSerializer(serializers.Serializer):

    new_password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True
    )
    old_password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        fields = ('password', 'password2')


    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

    def validate_new_password(self, value):
        if validate_password(value):
            return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('new_password'))
        instance.save()
        return instance
