from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    birth_date = models.DateField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    animal_species = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100, default="medicine")

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.animal.name}"
