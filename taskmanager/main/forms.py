from .models import Task, Clients
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['SurName', 'name', 'Patronymic', 'Number', 'Comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите имя',
                'class': 'form-control'
            }),
            'SurName': forms.TextInput(attrs={
                'placeholder': 'Введите Фамилию',
                'class': 'form-control'
            }),
            'Patronymic': forms.TextInput(attrs={
                'placeholder': 'Введите Отчество',
                'class': 'form-control'
            }),
            'Number': forms.TextInput(attrs={
                'placeholder': 'Введите номер',
                'class': 'form-control'
            }),
            'Comment': forms.Textarea(attrs={
                'placeholder': 'Ваш комментарий',
                'class': 'form-control',
                'style': 'height: 100px'
            }),

        }
