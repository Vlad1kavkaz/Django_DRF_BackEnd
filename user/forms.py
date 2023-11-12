import datetime
from datetime import timezone

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from main import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    # Новые поля для данных о животном
    pet_name = forms.CharField(label='Имя животного', widget=forms.TextInput(attrs={'class': 'form-input'}))
    pet_species = forms.CharField(label='Вид животного', widget=forms.TextInput(attrs={'class': 'form-input'}))
    pet_breed = forms.CharField(label='Порода животного', widget=forms.TextInput(attrs={'class': 'form-input'}))
    pet_birth_date = forms.DateTimeField(label='Дата рождения животного',
                                     widget=forms.DateTimeInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'pet_name', 'pet_species', 'pet_breed', 'pet_birth_date')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class EditUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['name', 'phone', 'email']
        labels = {
            'name': 'Логин',
            'phone': 'Телефон',
            'email': 'Почта',
        }
        error_messages = {
            'name': {
                'required': 'Пожалуйста, введите логин.',
            },
            'phone': {
                'required': 'Пожалуйста, введите телефон.',
            },
            'email': {
                'required': 'Пожалуйста, введите почту.',
                'invalid': 'Пожалуйста, введите корректную почту.',
            },
        }



class EditAnimalForm(forms.ModelForm):
    class Meta:
        model = models.Animal
        fields = ['name', 'species', 'breed', 'birth_date']
        labels = {
            'name': 'Кличка',
            'species': 'Вид',
            'breed': 'Порода',
            'birth_date': 'Дата рождения',
        }
        error_messages = {
            'name': {
                'required': 'Пожалуйста, введите кличку.',
            },
            'species': {
                'required': 'Пожалуйста, введите вид.',
            },
            'breed': {
                'required': 'Пожалуйста, введите породу.',
            },
            'birth_date': {
                'required': 'Пожалуйста, введите дату рождения.',
                'invalid': 'Пожалуйста, введите корректную дату рождения.',
            },
        }

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date and birth_date > datetime.date.today():
            raise ValidationError(_('Invalid date - birth date cannot be in the future'))
        return birth_date