from django.shortcuts import render, redirect
from .forms import TravelForm
from .models import travels
# Create your views here.
def index(request):
    travel = travels.objects.all()
    context = {
        'travels': travel
    }
    return render(request, 'travels/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:index')
    else:
        form = TravelForm()
    context = {
        'form' : form,
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = travels.objects.get(pk=pk)
    context = {
        'travel': travel
    }
    return render(request, 'travels/detail.html', context)