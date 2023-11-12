from rest_framework import serializers
from main.models import Service, Animal, Client, Appointment



class AllServiceSerializator(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'