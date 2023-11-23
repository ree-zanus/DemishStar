from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Clients
from .forms import AddPostForm
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

def categories(request):
    return HttpResponse("<h1>СТатьи по категориям</h1>")

def show_post(request, post_id):
    post = get_object_or_404(Task, pk=post_id)
    return HttpResponse(f"Отоброжение статьи с id = {post_id}")

def order(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
            #    Clients.objects.create(**form.cleaned_data)
            #    return redirect('home')
            #except:
            #    form.add_error(None, "Ошибка добавления поста")
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'form': form
    }
    return render(request, 'main/order.html', data)