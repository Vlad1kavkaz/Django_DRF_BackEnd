from django.urls import path
from .views import (ServiceListAPIView,
                    FilteredServiceListAPIView,
                    ClientListAPIView,
                    AppointmentListAPIView,
                    AnimalListAPIView,
                    FilteredClientListAPIView,
                    FilteredAnimalListAPIView,
                    FilteredAppointmentListAPIView)

urlpatterns = [
    path('get-all-services/',ServiceListAPIView.as_view(), name='get-all-service'),
    path('get-service-for/', FilteredServiceListAPIView.as_view(), name='get-for-service'),

    path('get-all-client/',ClientListAPIView.as_view(), name='get-all-client'),
    path('get-client-for/', FilteredClientListAPIView.as_view(), name='get-for-client'),

    path('get-all-animel/', AnimalListAPIView.as_view(), name='get-all-animel'),
    path('get-animal-for/', FilteredAnimalListAPIView.as_view(), name='get-animal-for'),

    path('get-all-appointment/', AppointmentListAPIView.as_view(), name='get-all-appointment'),
    path('get-appointment-for/', FilteredAppointmentListAPIView.as_view(), name='get-appointment-for'),

]