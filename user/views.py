from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from main import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegisterUserForm, LoginUserForm, EditClientForm, EditAnimalForm, EditUserForm
from main.models import Client, Animal, Appointment

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user\\register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        redirect_to = self.request.GET.get('next', reverse_lazy(settings.LOGIN_REDIRECT_URL))

        # Создание пользователя
        user = form.save()

        # Создание клиента
        client = models.Client.objects.create(
            name=form.cleaned_data['username'],  # Используйте нужные поля
            phone='',
            email=form.cleaned_data['email'],
            user=user
        )

        # Создание животного
        pet = models.Animal.objects.create(
            name=form.cleaned_data['pet_name'],
            species=form.cleaned_data['pet_species'],
            breed=form.cleaned_data['pet_breed'],
            birth_date=form.cleaned_data['pet_birth_date'],
            owner=client
        )

        # Дополнительные действия, если необходимо

        login(self.request, form.get_user())
        return HttpResponseRedirect(redirect_to)



class loginUser(LoginView):
    template_name = 'user\\login.html'
    form_class = LoginUserForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистрация'
        context['cat_selected'] = 0

        return context



def logout_user(request):
    logout(request)
    return redirect('home_page')

class AccountView(FormView):
    template_name = 'user\\account.html'
    form_class = EditClientForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        # Обработка формы редактирования клиента
        client = Client.objects.get(user=self.request.user)
        client.name = form.cleaned_data['name']
        client.phone = form.cleaned_data['phone']
        client.email = form.cleaned_data['email']
        client.save()
        return super().form_valid(form)

    def get_initial(self):
        # Начальные данные для формы редактирования клиента
        client = Client.objects.get(user=self.request.user)
        return {'name': client.name, 'phone': client.phone, 'email': client.email}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем данные о животных пользователя в контекст
        client = Client.objects.get(user=self.request.user)
        animals = Animal.objects.filter(owner=client)
        appointments = Appointment.objects.filter(animal__in=animals)
        appointments_data = {}
        for animal in animals:
            animal_appointments = appointments.filter(animal=animal)
            appointments_data[animal.name] = [{'date': appointment.date, 'service': appointment.service.name} for
                                              appointment in animal_appointments]
        context['client'] = client
        context['animals'] = animals
        context['appointments'] = appointments_data
        return context

@login_required(login_url='login')
def account(request):
    return AccountView.as_view()(request)

@login_required(login_url='login')
def add_animal(request):
    animal_form = EditAnimalForm()

    if request.method == "POST":
        animal_form = EditAnimalForm(request.POST)

        if animal_form.is_valid():
            animal = animal_form.save(commit=False)
            animal.owner = request.user.client
            animal.save()
            return redirect('account')

    return render(request, 'user/add_animal.html', {'animal_form': animal_form})


from pprint import pprint


@login_required(login_url='login')
def edit_account(request):
    user_form = EditUserForm(instance=request.user)
    animal_forms = []

    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            print("User form saved successfully.")
        else:
            print("User form is not valid.")
            pprint(user_form.errors)

        for animal in Animal.objects.filter(owner=request.user.client):
            form = EditAnimalForm(request.POST, instance=animal, prefix=f'animal_{animal.id}')
            if form.is_valid():
                animal_instance = form.save(commit=False)
                animal_instance.save()
                animal_forms.append((animal_instance, form))
                print(f"Animal form for {animal_instance} saved successfully.")
            else:
                animal_forms.append((animal, form))
                print(f"Animal form for {animal_instance} is not valid.")
                pprint(form.errors)

        return redirect('account')

    else:
        # Используйте форму без POST-данных для отображения данных клиента
        user_form = EditUserForm(instance=request.user)

        # Добавьте существующие животные и их формы
        for animal in Animal.objects.filter(owner=request.user.client):
            form = EditAnimalForm(instance=animal, prefix=f'animal_{animal.id}')
            animal_forms.append((animal, form))

    return render(request, 'user/edit_profile.html', {'user_form': user_form, 'animal_forms': animal_forms})




