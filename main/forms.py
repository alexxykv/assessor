from .models import Main
from django.forms import ModelForm, TextInput, DateInput, EmailInput, URLInput


class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = [
            'firstName',
            'lastName',
            'patronymic',
            'date_birth',
            'phone_number',
            'city',
            'email',
            'site_1',
            'site_2',
            'site_3',
            'site_4',
            'site_5',
            'site_6',
            'site_7',
            'site_8',
            'site_9',
            'site_10'
        ]

        widgets = {
            'firstName': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иван'
            }),
            'lastName': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов'
            }),
            'patronymic': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванович'
            }),
            'date_birth': DateInput(attrs={
                'class': 'form-control',
                'placeholder': '01.01.1999',
                'type': 'date',
                'min': '1900-01-01',
                'value': '1900-01-01'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Москва'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control mask-phone',
                'placeholder': '+7 (123) 456-23-12'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@domen.com'
            }),
            'site_1': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_2': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_3': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_4': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_5': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_6': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_7': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_8': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_9': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'site_10': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            })
        }