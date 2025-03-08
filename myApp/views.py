from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, "signup.html", context)

def loginpage(request):
    form = UserCreationForm(request.POST)
    context = {'form': form}
    return render(request, "loginpage.html", context)
    

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def agents(request):
    return render(request, 'agents.html')

def contact(request):
    return render(request, 'contact.html')

def properties(request):
    return render(request, 'properties.html')

def property_single(request):
    return render(request, 'property_single.html')

def service_details(request):
    return render(request, 'service_details.html')

def services(request):
    return render(request, 'services.html')

def starter_page(request):
    return render(request, 'starter_page.html')

