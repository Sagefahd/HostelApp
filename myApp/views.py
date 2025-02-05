from django.shortcuts import render

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
    return render(request, 'property-single.html')

def service_details(request):
    return render(request, 'service_details.html')

def services(request):
    return render(request, 'services.html')

def starter_page(request):
    return render(request, 'starter_page.html')

# Create your views here.
