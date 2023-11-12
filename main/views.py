from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from datetime import datetime, timedelta
import random

from . import models


def home(request):
    clients = models.Client.objects.all()
    '''for client in clients:
        animal1 = models.Animal.objects.create(
            name=random.choices(['Мурзик', 'Леон', 'Даша', 'Корни', 'Мухтар', 'Амстер', 'Штрудель', 'Рыжик', 'Мурка']),
            species=random.choices(['Кошка', 'Кошка', 'Кошка', 'Кошка', 'Собака', 'Попугай']), breed="",
            birth_date=f"{random.randint(1, 29)}.{random.randint(1, 12)}.{random.randint(2000, 2022)}", owner=client)
        animal2 = models.Animal.objects.create(
            name=random.choices(['Волан-де-Морт', 'Фунтик', 'Доллар', 'Оливка', 'Джуси', 'Клэй', 'Фараон', 'Олимп', 'Зумба', 'Виски']),
            species=random.choices(['Собака', 'Собака', 'Собака', 'Собака', 'Кошка', 'Лошадь']), breed="",
            birth_date=f"{random.randint(1, 29)}.{random.randint(1, 12)}.{random.randint(2000, 2022)}",
            owner=client)'''
    '''
    service1 = models.Service.objects.create(name="Стрижка", animal_species="Собака", price="1200.00", category="Груминг")
    service2 = models.Service.objects.create(name="Стрижка", animal_species="Кошка", price="1000.00", category="Груминг")
    service5 = models.Service.objects.create(name="Стрижка", animal_species="Лошадь", price="3000.00", category="Груминг")
    service3 = models.Service.objects.create(name="Чистка зубов", animal_species="Кошка", price="300.00", category="Груминг")
    service4 = models.Service.objects.create(name="Чистка зубов", animal_species="Собака", price="500.00", category="Груминг")
    service6 = models.Service.objects.create(name="Чистка зубов", animal_species="Лошадь", price="1000.00", category="Груминг")
    service7 = models.Service.objects.create(name="Обработка ушей", animal_species="Кошка", price="200.00", category="Груминг")
    service8 = models.Service.objects.create(name="Обработка ушей", animal_species="Собака", price="400.00", category="Груминг")
    service9 = models.Service.objects.create(name="Обработка ушей", animal_species="Лошадь", price="1000.00", category="Груминг")
    service10 = models.Service.objects.create(name="Стрижка когтей", animal_species="Кошка", price="500.00", category="Груминг")
    service31 = models.Service.objects.create(name="Стрижка когтей", animal_species="Попугай", price="500.00", category="Груминг")
    service11 = models.Service.objects.create(name="Стрижка когтей", animal_species="Собака", price="700.00", category="Груминг")
    service12 = models.Service.objects.create(name="Обработка копыт", animal_species="Лошадь", price="5000.00", category="Груминг")
    service13 = models.Service.objects.create(name="Вычесывание", animal_species="Кошка", price="1000.00", category="Груминг")
    service14 = models.Service.objects.create(name="Вычесывание", animal_species="Собака", price="1500.00", category="Груминг")
    service15 = models.Service.objects.create(name="Вычесывание", animal_species="Лошадь", price="5000.00", category="Груминг")
    service16 = models.Service.objects.create(name="Комплекс (Помывка,Вычёсывание,Стрижка,Стрижка когтей,Обработка ушей, Сушка", animal_species="Кошка", price="3000.00", category="Груминг")
    service17 = models.Service.objects.create(name="Комплекс (Помывка,Вычёсывание,Стрижка,Стрижка когтей,Обработка ушей, Сушка", animal_species="Собака", price="4000.00", category="Груминг")
    service18 = models.Service.objects.create(name="Комплекс (Помывка,Вычёсывание,Стрижка,Стрижка когтей,Обработка ушей, Сушка", animal_species="Лошадь", price="10000.00", category="Груминг")

    service19 = models.Service.objects.create(name="Чипирование", animal_species="Кошка", price="3000.00", category="Чипирование")
    service20 = models.Service.objects.create(name="Чипирование", animal_species="Собака", price="3500.00", category="Чипирование")
    service27 = models.Service.objects.create(name="Чипирование", animal_species="Попугай", price="3000.00", category="Чипирование")
    service21 = models.Service.objects.create(name="Чипирование", animal_species="Лошадь", price="5000.00", category="Чипирование")

    service22 = models.Service.objects.create(name="Вакцинация", animal_species="Кошка", price="3000.00", category="Вакцинация")
    service23 = models.Service.objects.create(name="Вакцинация", animal_species="Собака", price="3200.00", category="Вакцинация")
    service24 = models.Service.objects.create(name="Вакцинация", animal_species="Лошадь", price="5000.00", category="Вакцинация")
    service30 = models.Service.objects.create(name="Вакцинация", animal_species="Попугай", price="3000.00", category="Вакцинация")

    service25 = models.Service.objects.create(name="Кастрация,Стерилизация", animal_species="Кошка", price="3000.00", category="Хирургия")
    service26 = models.Service.objects.create(name="Кастрация,Стерилизация", animal_species="Собака", price="3400.00", category="Хирургия")
    service28 = models.Service.objects.create(name="Кастрация,Стерилизация", animal_species="Попугай", price="3500.00", category="Хирургия")
    service29 = models.Service.objects.create(name="Кастрация,Стерилизация", animal_species="Лошадь", price="7500.00", category="Хирургия")
    service39 = models.Service.objects.create(name="Удаление опухоли", animal_species="Лошадь", price="10500.00", category="Хирургия")
    service32 = models.Service.objects.create(name="Удаление опухоли", animal_species="Попугай", price="3500.00", category="Хирургия")
    service33 = models.Service.objects.create(name="Удаление опухоли", animal_species="Кошка", price="5500.00", category="Хирургия")
    service34 = models.Service.objects.create(name="Удаление опухоли", animal_species="Собака", price="7500.00", category="Хирургия")
    service35 = models.Service.objects.create(name="Обработка ран", animal_species="Лошадь", price="1500.00", category="Хирургия")
    service36 = models.Service.objects.create(name="Обработка ран", animal_species="Кошка", price="400.00", category="Хирургия")
    service37 = models.Service.objects.create(name="Обработка ран", animal_species="Собака", price="500.00", category="Хирургия")
    service38 = models.Service.objects.create(name="Обработка ран", animal_species="Попугай", price="200.00", category="Хирургия")
    service40 = models.Service.objects.create(name="Трамватология", animal_species="Попугай", price="500.00", category="Хирургия")
    service41 = models.Service.objects.create(name="Трамватология", animal_species="Кошка", price="700.00", category="Хирургия")
    service42 = models.Service.objects.create(name="Трамватология", animal_species="Собака", price="1000.00", category="Хирургия")
    service43 = models.Service.objects.create(name="Трамватология", animal_species="Лошадь", price="2000.00", category="Хирургия")
    service44 = models.Service.objects.create(name="Операции на ЖКТ", animal_species="Попугай", price="2000.00", category="Хирургия")
    service45 = models.Service.objects.create(name="Операции на ЖКТ", animal_species="Лошадь", price="8000.00", category="Хирургия")
    service46 = models.Service.objects.create(name="Операции на ЖКТ", animal_species="Собака", price="5000.00", category="Хирургия")
    service47 = models.Service.objects.create(name="Операции на ЖКТ", animal_species="Кошка", price="4000.00", category="Хирургия")

    service48 = models.Service.objects.create(name="Общий анализ мочи", animal_species="Кошка", price="400.00", category="Лабораторные исследования")
    service49 = models.Service.objects.create(name="Общий анализ мочи", animal_species="Собака", price="500.00", category="Лабораторные исследования")
    service50 = models.Service.objects.create(name="Общий анализ мочи", animal_species="Попугай", price="400.00", category="Лабораторные исследования")
    service51 = models.Service.objects.create(name="Общий анализ мочи", animal_species="Лошадь", price="1000.00", category="Лабораторные исследования")
    service52 = models.Service.objects.create(name="Общий анализ кала", animal_species="Кошка", price="600.00", category="Лабораторные исследования")
    service53 = models.Service.objects.create(name="Общий анализ кала", animal_species="Собака", price="700.00", category="Лабораторные исследования")
    service54 = models.Service.objects.create(name="Общий анализ кала", animal_species="Попугай", price="600.00", category="Лабораторные исследования")
    service55 = models.Service.objects.create(name="Общий анализ кала", animal_species="Лошадь", price="1300.00", category="Лабораторные исследования")
    service56 = models.Service.objects.create(name="Общий клинический анализ крови", animal_species="Кошка", price="600.00", category="Лабораторные исследования")
    service57 = models.Service.objects.create(name="Общий клинический анализ крови", animal_species="Собака", price="700.00", category="Лабораторные исследования")
    service58 = models.Service.objects.create(name="Общий клинический анализ крови", animal_species="Попугай", price="600.00", category="Лабораторные исследования")
    service59 = models.Service.objects.create(name="Общий клинический анализ крови", animal_species="Лошадь", price="900.00", category="Лабораторные исследования")

    service60 = models.Service.objects.create(name="Лечение заболеваний глаз", animal_species="Кошка", price="1000.00", category="Офтальмология")
    service61 = models.Service.objects.create(name="Лечение заболеваний глаз", animal_species="Собака", price="1300.00", category="Офтальмология")
    service62 = models.Service.objects.create(name="Лечение заболеваний глаз", animal_species="Попугай", price="1000.00", category="Офтальмология")
    service63 = models.Service.objects.create(name="Лечение заболеваний глаз", animal_species="Лошадь", price="1600.00", category="Офтальмология")
    service64 = models.Service.objects.create(name="Офтальмологический осмотр и консультация", animal_species="Лошадь", price="1600.00", category="Офтальмология")
    service65 = models.Service.objects.create(name="Офтальмологический осмотр и консультация", animal_species="Собака", price="1300.00", category="Офтальмология")
    service66 = models.Service.objects.create(name="Офтальмологический осмотр и консультация", animal_species="Кошка", price="1000.00", category="Офтальмология")
    service67 = models.Service.objects.create(name="Офтальмологический осмотр и консультация", animal_species="Попугай", price="1000.00", category="Офтальмология")
    service68 = models.Service.objects.create(name="Диагностические процедуры", animal_species="Попугай", price="1000.00", category="Офтальмология")
    service69 = models.Service.objects.create(name="Диагностические процедуры", animal_species="Лошадь", price="3000.00", category="Офтальмология")
    service70 = models.Service.objects.create(name="Диагностические процедуры", animal_species="Кошка", price="1000.00", category="Офтальмология")
    service71 = models.Service.objects.create(name="Диагностические процедуры", animal_species="Собака", price="1500.00", category="Офтальмология")

    service72 = models.Service.objects.create(name="Оральный осмотр и консультация", animal_species="Собака", price="500.00", category="Стоматология")
    service73 = models.Service.objects.create(name="Оральный осмотр и консультация", animal_species="Кошка", price="400.00", category="Стоматология")
    service74 = models.Service.objects.create(name="Оральный осмотр и консультация", animal_species="Попугай", price="400.00", category="Стоматология")
    service75 = models.Service.objects.create(name="Оральный осмотр и консультация", animal_species="Лошадь", price="1000.00", category="Стоматология")
    service76 = models.Service.objects.create(name="Лечение зубных кариесов и полостей", animal_species="Собака", price="1500.00", category="Стоматология")
    service77 = models.Service.objects.create(name="Лечение зубных кариесов и полостей", animal_species="Кошка", price="1300.00", category="Стоматология")
    service78 = models.Service.objects.create(name="Лечение зубных кариесов и полостей", animal_species="Лошадь", price="3000.00", category="Стоматология")
    service79 = models.Service.objects.create(name="Экстракция (удаление) зубов", animal_species="Собака", price="500.00", category="Стоматология")
    service80 = models.Service.objects.create(name="Экстракция (удаление) зубов", animal_species="Кошка", price="500.00", category="Стоматология")
    service81 = models.Service.objects.create(name="Экстракция (удаление) зубов", animal_species="Лошадь", price="1000.00", category="Стоматология")
    service82 = models.Service.objects.create(name="Предоставление рекомендаций по уходу", animal_species="Собака", price="500.00", category="Стоматология")
    service83 = models.Service.objects.create(name="Предоставление рекомендаций по уходу", animal_species="Кошка", price="500.00", category="Стоматология")
    service84 = models.Service.objects.create(name="Предоставление рекомендаций по уходу", animal_species="Попугай", price="500.00", category="Стоматология")
    service85 = models.Service.objects.create(name="Предоставление рекомендаций по уходу", animal_species="Лошадь", price="500.00", category="Стоматология")
    service86 = models.Service.objects.create(name="Удаление наростов и деформаций клюва", animal_species="Попугай", price="500.00", category="Стоматология")
    service87 = models.Service.objects.create(name="Обрезка и полировка клюва", animal_species="Попугай", price="500.00", category="Стоматология")
    service88 = models.Service.objects.create(name="Лечение заболеваний клюва", animal_species="Попугай", price="500.00", category="Стоматология")

    service89 = models.Service.objects.create(name="Введения лекарственных препаратов", animal_species="Попугай", price="500.00", category="Терапия")
    service90 = models.Service.objects.create(name="Введения лекарственных препаратов", animal_species="Кошка", price="500.00", category="Терапия")
    service91 = models.Service.objects.create(name="Введения лекарственных препаратов", animal_species="Собака", price="500.00", category="Терапия")
    service92 = models.Service.objects.create(name="Введения лекарственных препаратов", animal_species="Лошадь", price="1000.00", category="Терапия")
    service93 = models.Service.objects.create(name="Физиотерапия", animal_species="Лошадь", price="5000.00", category="Терапия")
    service94 = models.Service.objects.create(name="Физиотерапия", animal_species="Собака", price="4000.00", category="Терапия")
    service95 = models.Service.objects.create(name="Физиотерапия", animal_species="Кошка", price="3000.00", category="Терапия")
    service96 = models.Service.objects.create(name="Физиотерапия", animal_species="Попугай", price="3000.00", category="Терапия")
    service97 = models.Service.objects.create(name="Реабилитация", animal_species="Попугай", price="3000.00", category="Терапия")
    service98 = models.Service.objects.create(name="Реабилитация", animal_species="Кошка", price="3000.00", category="Терапия")
    service99 = models.Service.objects.create(name="Реабилитация", animal_species="Собака", price="4000.00", category="Терапия")
    service100 = models.Service.objects.create(name="Реабилитация", animal_species="Лошадь", price="6000.00", category="Терапия")

    service101 = models.Service.objects.create(name="Оформление документов", animal_species="Лошадь", price="1000.00", category="Оформелние ветеринарных сопроводительных документов")
    service102 = models.Service.objects.create(name="Оформление документов", animal_species="Кошка", price="1000.00", category="Оформелние ветеринарных сопроводительных документов")
    service103 = models.Service.objects.create(name="Оформление документов", animal_species="Собака", price="1000.00", category="Оформелние ветеринарных сопроводительных документов")
    service104 = models.Service.objects.create(name="Оформление документов", animal_species="Попугай", price="1000.00", category="Оформелние ветеринарных сопроводительных документов")

    service105 = models.Service.objects.create(name="Зоогостиница (за 1 день)", animal_species="Лошадь", price="5000.00", category="Зоогостиница")
    service106 = models.Service.objects.create(name="Зоогостиница (за 1 день)", animal_species="Собака", price="3000.00", category="Зоогостиница")
    service107 = models.Service.objects.create(name="Зоогостиница (за 1 день)", animal_species="Кошка", price="2000.00", category="Зоогостиница")
    service108 = models.Service.objects.create(name="Зоогостиница (за 1 день)", animal_species="Попугай", price="2000.00", category="Зоогостиница")
'''
    services = models.Service.objects.all()
    print(len(services))
    return render(request, 'main/home.html')

def home_page(request):
    return render(request, 'main/home.html')

class Search(ListView):
    template_name = 'main/search.html'
    context_object_name = 'product'
    def get_queryset(self):
        return models.Animal.objects.filter(name__icontains=self.request.GET.get('q'))

def search(request):
    search_input = request.GET.get('q')

    service = models.Service.objects.filter(Q(name__iregex=r'\b{}\b'.format(search_input)) |
                                            Q(category__iregex=r'\b{}\b'.format(search_input)) |
                                            Q(animal_species__iregex=r'\b{}\b'.format(search_input)))

    return render(request, 'main/search.html', {'product': service})

def about(request):
    return render(request, 'main/about.html')

def grumming(request):
    grumming = models.Service.objects.filter(Q(category__iregex=r'\b{}\b'.format('Груминг')))
    return render(request, 'main/grumming.html', {'grumming':grumming})


def vaccine(request):
    vaccine = models.Service.objects.filter(Q(category__iregex=r'\b{}\b'.format('Вакцинация')))
    return render(request, 'main/vaccine.html', {'vaccine':vaccine})

def hirurg(request):
    hirurg = models.Service.objects.filter(Q(category__iregex=r'\b{}\b'.format('Хирургия')))
    return render(request, 'main/hirurg.html', {'hirurg':hirurg})


def labis(request):
    labis = models.Service.objects.filter(Q(category__iregex=r'\b{}\b'.format('Лабораторные исследования')))
    return render(request, 'main/labis.html', {'labis':labis})


def chip(request):
    chip = models.Service.objects.filter(Q(category__iregex=r'\b{}\b'.format('Чипирование')))
    return render(request, 'main/chip.html', {'chip':chip})


def terap(request):
    terap = models.Service.objects.filter(Q(category__iregex=r'\b{}\b'.format('Терапия')))
    return render(request, 'main/terap.html', {'terap':terap})


def oftal(request):
    oftal = models.Service.objects.filter(Q(category__iregex=r'\b{}\b'.format('Офтальмология')))
    return render(request, 'main/oftal.html', {'oftal':oftal})

def update_db(request):
    animals = models.Animal.objects.all()

    def generate_random_dog_breed():
        dog_breeds = ['Лабрадор', 'Немецкая овчарка', 'Золотистый ретривер', 'Бульдог', 'Пудель',
                      'Хаски', 'Доберман', 'Ротвейлер', 'Чихуахуа', 'Мопс']
        return random.choice(dog_breeds)

    # Функция для генерации случайной породы для кошки
    def generate_random_cat_breed():
        cat_breeds = ['Сиамская', 'Персидская', 'Мейн-кун', 'Рагдолл', 'Бенгальская',
                      'Сфинкс', 'Британская короткошерстная', 'Абиссинская', 'Манчкин', 'Норвежская лесная']
        return random.choice(cat_breeds)
    # Функция для генерации случайной породы для лошади
    def generate_random_horse_breed():
        horse_breeds = ['Тороугбред', 'Квартерхорс', 'Арабская', 'Аппалуза', 'Клайдсдейл']
        return random.choice(horse_breeds)

    # Функция для генерации случайной породы для попугая
    def generate_random_parrot_breed():
        parrot_breeds = ['Буджеригар', 'Какаду', 'Африканский серый', 'Ара', 'Конюр']
        return random.choice(parrot_breeds)

    for animal in animals:
        if animal.species == 'Собака':
            animal.breed = generate_random_dog_breed()

        elif animal.species == 'Кошка':
            animal.breed = generate_random_cat_breed()

        elif animal.species == 'Лошадь':
            animal.breed = generate_random_horse_breed()

        elif animal.species == 'Попугай':
            animal.breed = generate_random_parrot_breed()

        # Сохраняем изменения
        animal.save()

    return render(request, 'main/layout.html')
