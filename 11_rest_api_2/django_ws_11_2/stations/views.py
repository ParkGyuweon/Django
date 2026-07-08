from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Location, Station
from .serializers import LocationListSerializer, LocationSerializer, StationListSerializer, StationSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def station_list(request, location_pk=None):
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationListSerializer(stations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        location = Location.objects.get(pk=location_pk)
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(address=location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def station_detail(request, station_pk):
    station = Station.objects.get(pk=station_pk)
    serializer = StationSerializer(station)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def location_list(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationListSerializer(locations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)