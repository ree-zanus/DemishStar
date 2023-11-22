from .models import Task, Clients
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class AddPostForm(forms.Form):
    SurName = forms.CharField(max_length=50, label="Фамилия: ")
    name = forms.CharField(max_length=50, label="Имя: ")
    Patronymic = forms.CharField(max_length=50, label="Отчество: ")
    Number = forms.CharField(max_length=10, label="Номер телефона: ")
