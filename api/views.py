from rest_framework import generics
from rest_framework.response import Response
from main.models import Service, Client, Appointment, Animal
from .serializer import AllServiceSerializator, ClientSerializer, AnimalSerializer, AppointmentSerializer

class ServiceListAPIView(generics.ListAPIView):
    serializer_class = AllServiceSerializator

    def get_queryset(self):
        return Service.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FilteredServiceListAPIView(generics.ListAPIView):
    serializer_class = AllServiceSerializator

    def get_queryset(self):
        queryset = Service.objects.all()

        # Получаем параметры запроса
        category = self.request.query_params.get('category', '')
        animal_species = self.request.query_params.get('animal_species', '')
        price = self.request.query_params.get('price', '')
        name = self.request.query_params.get('name', '')

        # Фильтрация по категории
        if category:
            queryset = queryset.filter(category=category)

        # Фильтрация по виду животного
        if animal_species:
            queryset = queryset.filter(animal_species=animal_species)

        # Фильтрация по цене
        if price:
            queryset = queryset.filter(price=price)

        if name:
            queryset = queryset.filter(name=name)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AnimalListAPIView(generics.ListAPIView):
    serializer_class = AnimalSerializer

    def get_queryset(self):
        return Animal.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AppointmentListAPIView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FilteredClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.all()

        # Получаем параметры запроса
        user = self.request.query_params.get('user', '')
        name = self.request.query_params.get('name', '')
        phone = self.request.query_params.get('phone', '')
        email = self.request.query_params.get('email', '')

        # Фильтрация по категории
        if user:
            queryset = queryset.filter(user=user)

        # Фильтрация по виду животного
        if name:
            queryset = queryset.filter(name=name)

        # Фильтрация по цене
        if phone:
            queryset = queryset.filter(phone=phone)

        if email:
            queryset = queryset.filter(email=email)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FilteredAppointmentListAPIView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        date = self.request.query_params.get('date', None)
        animal_name = self.request.query_params.get('animal_name', None)
        service_name = self.request.query_params.get('service_name', None)

        if date:
            queryset = queryset.filter(date=date)

        if animal_name:
            queryset = queryset.filter(animal__name=animal_name)

        if service_name:
            queryset = queryset.filter(service__name=service_name)

        return queryset

class FilteredAnimalListAPIView(generics.ListAPIView):
    serializer_class = AnimalSerializer

    def get_queryset(self):
        queryset = Animal.objects.all()
        name = self.request.query_params.get('name', None)
        species = self.request.query_params.get('species', None)
        breed = self.request.query_params.get('breed', None)
        birth_date = self.request.query_params.get('birth_date', None)

        if name:
            queryset = queryset.filter(name=name)

        if species:
            queryset = queryset.filter(species=species)

        if breed:
            queryset = queryset.filter(breed=breed)

        if birth_date:
            queryset = queryset.filter(birth_date=birth_date)

        return queryset