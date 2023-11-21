from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def cart(request):
    tasks = Task.objects.all()
    return render(request, 'main/cart.html', {'tasks': tasks})

def cartItem(request, my_id):
    item = Task.objects.get(id=my_id)
    context = {
        'item': item
    }
    return render(request, 'main/detail.html', context=context)

def order(request):
    return render(request, 'main/order.html')