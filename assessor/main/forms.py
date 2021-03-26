from .models import Main
from django.forms import ModelForm, TextInput, DateInput, URLInput, EmailInput

class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ['name', 'date_birth', 'phone_number', 'email', 'city', 'site_1', 'site_2', 'site_3', 'site_4', 'site_5', 'site_6', 'site_7', 'site_8', 'site_9', 'site_10']

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
            'site_1': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 1'
            }),
            'site_2': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 2'
            }),
            'site_3': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 3'
            }),
            'site_4': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 4'
            }),
            'site_5': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 5'
            }),
            'site_6': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 6'
            }),
            'site_7': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 7'
            }),
            'site_8': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 8'
            }),
            'site_9': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 9'
            }),
            'site_10': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сайт 10'
            })
        }
