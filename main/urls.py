
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home_page, name='home_page'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('grumming/', views.grumming, name='grumming'),
    path('vaccine/', views.vaccine, name='vaccine'),
    path('hirurg/', views.hirurg, name='hirurg'),
    path('chip/', views.chip, name='chip'),
    path('oftal/', views.oftal, name='oftal'),
    path('stomat/', views.hirurg, name='stomat'),
    path('labis/', views.labis, name='labis'),
    path('terap/', views.terap, name='terap'),
    path('zoog/', views.hirurg, name='zoog'),
    path('doc/', views.hirurg, name='doc'),

    #path('update_db', views.update_db, name='create'),
]
