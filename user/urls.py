from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.loginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.AccountView.as_view(), name='account'),
    path('add/', views.add_animal, name='add_animal'),
    path('edit/', views.edit_account, name='edit'),
]

