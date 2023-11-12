from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from main import models


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    # Новые поля для данных о животном
    pet_name = forms.CharField(label='Имя животного', widget=forms.TextInput(attrs={'class': 'form-input'}))
    pet_species = forms.CharField(label='Вид животного', widget=forms.TextInput(attrs={'class': 'form-input'}))
    pet_breed = forms.CharField(label='Порода животного', widget=forms.TextInput(attrs={'class': 'form-input'}))
    pet_birth_date = forms.CharField(label='Дата рождения животного',
                                     widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'pet_name', 'pet_species', 'pet_breed', 'pet_birth_date')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class EditUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['name', 'phone', 'email']


class EditAnimalForm(forms.ModelForm):
    class Meta:
        model = models.Animal
        fields = ['name', 'species', 'breed', 'birth_date']
