from .models import Main
from django.forms import ModelForm, TextInput, DateInput, EmailInput

class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ['name', 'date_birth', 'phone_number', 'email', 'city', 'site_1', 'site_2', 'site_3']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            'date_birth': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            'site_1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 1'
            }),
            'site_2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 2'
            }),
            'site_3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 3'
            })
        }
