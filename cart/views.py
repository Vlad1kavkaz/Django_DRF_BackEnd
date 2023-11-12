from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Service, Appointment
from django.contrib import messages
from .cart import Cart
from .forms import CartAddProductForm, AddressForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Service, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=1)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Service, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})

    context = {'cart': cart, 'products': cart.cart.values()}  # Добавьте 'products' в контекст

    return render(request, 'cart/detail.html', context)



def order_show(request):
    cart = Cart(request)
    initial_values = {'adress': 'Самовывоз'}
    form = AddressForm(request.user, request.POST or None, initial=initial_values)
    error_message = None  # Инициализируем переменную для хранения сообщения об ошибке

    if request.method == 'POST':
        if form.is_valid():
            time_date = form.cleaned_data['time_date']
            selected_animal = form.cleaned_data['animal']

            # Проверка соответствия видов животного и услуги
            for serv in cart:
                service = serv['product']
                if service.animal_species != selected_animal.species:
                    error_message = 'Выбранное животное не соответствует виду услуги.'
                    break

            if not error_message:
                # Создание объекта Appointment
                for serv in cart:
                    service = serv['product']
                    appointment = Appointment.objects.create(
                        date=time_date,
                        animal=selected_animal,
                        service=service
                    )

                for item in cart:
                    cart_remove(request, item['product'].id)

                return redirect('home_page')

    # Передаем сообщение об ошибке в контекст шаблона
    return render(request, 'cart/order.html', {'cart': cart, 'form': form, 'error_message': error_message})