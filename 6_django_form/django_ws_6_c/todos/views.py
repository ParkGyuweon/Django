from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    
    context = {
        'form' : form
    }
    return render(request, 'todos/create.html', context)
    
def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:index')
    return redirect('todos:detail', todo.pk)

def update(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
