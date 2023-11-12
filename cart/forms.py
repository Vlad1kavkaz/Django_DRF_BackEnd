from django import forms
from datetime import datetime
from main.models import Animal, Client

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 5)]


class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class AddressForm(forms.Form):
    # ... (ваш код)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            # Получите клиента, связанного с пользователем
            client = Client.objects.get(user=user)

            # Получите всех животных, связанных с этим клиентом
            client_animals = client.animal_set.all()

            # Добавьте выпадающий список для выбора животного
            self.fields['animal'] = forms.ModelChoiceField(
                queryset=client_animals,
                widget=forms.Select,
                label='Выберите вашего питомца',
                required=True
            )

        except Client.DoesNotExist:
            pass

    phonenumber = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        initial='+7'
    )
    time_date = forms.DateTimeField(
        label='Дата и время',
        widget=forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
    )
    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Введите комментарий к услуге, ваши пожелания, уточнения и прочее'})
    )
