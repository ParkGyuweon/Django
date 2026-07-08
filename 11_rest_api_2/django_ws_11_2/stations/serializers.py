from rest_framework import serializers
from .models import Station, Location

class StationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('address', 'is_opening',)

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
        read_only_fields = ('address',)

class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'