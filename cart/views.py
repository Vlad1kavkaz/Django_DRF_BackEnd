import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Service, Appointment
from django.contrib import messages

from .cart import Cart
from .forms import CartAddProductForm, AddressForm
from django.conf import settings


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Service, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=1)

    print
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

    if request.method == 'POST' and form.is_valid():
        phonenumber = form.cleaned_data['phonenumber']
        time_date = form.cleaned_data['time_date']
        email = request.user.email
        comment = form.cleaned_data['comment']

        # Получите выбранных животных из формы
        selected_animals = form.cleaned_data['animal']
        service = Service
        # Создайте новый экземпляр Appointment для каждого выбранного животного
        for serv in cart.__iter__():
            service = serv['product']
        appointment = Appointment.objects.create(
            date=time_date,
            animal=selected_animals,  # Используйте выбранное животное
            service=service # Замените на ваш объект Service
            )

        for item in cart.__iter__():
            cart_remove(request, item['product'].id)

        return redirect('home_page')

    return render(request, 'cart/order.html', {'cart': cart, 'form': form})