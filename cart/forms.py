from django import forms
from datetime import datetime
from main.models import Animal, Client

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 5)]


class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class AddressForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            client = Client.objects.get(user=user)
            client_animals = client.animal_set.all()
            self.fields['animal'] = forms.ModelChoiceField(
                queryset=client_animals,
                widget=forms.Select,
                label='Выберите вашего питомца',
                required=True
            )

        except Client.DoesNotExist:
            pass


    time_date = forms.DateTimeField(
        label='Дата и время',
        widget=forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
    )

