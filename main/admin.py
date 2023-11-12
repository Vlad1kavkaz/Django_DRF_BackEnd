from django.contrib import admin
from .models import Animal, Appointment, Service, Client

admin.site.register(Animal)
admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(Client)

