from rest_framework import serializers
from . import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


class TransportFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TransportFull
        fields = '__all__'


class GoodsCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GoodsCount
        fields = '__all__'
