from rest_framework import serializers
from .models import Driver, Adress, Vehicle, EntryRegister, ExitRegister, ParkingSpot

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    adress = AdressSerializer(many=True, read_only=True)
    vehicle = VehicleSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = '__all__'

class EntryRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryRegister
        fields = '__all__'

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'

class ExitRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExitRegister
        fields = '__all__'
