from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    model = get_user_model()
    users = model.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)