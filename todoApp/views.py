from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def home(request):
    context = {
        'todoItem': todoItem.objects.all(),
        'form': todoItemForm()
        }

    if request.method == 'POST':
        form = todoItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'home.html', context)


def updateTodo(request, pk):
    Item = todoItem.objects.get(id=pk)
    form = todoItemForm(instance=Item)

    if request.method == 'POST':
        form = todoItemForm(request.POST, instance=Item)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'update.html', context)


def deleteTodo(request, pk):
    item = todoItem.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'delete.html', context)

