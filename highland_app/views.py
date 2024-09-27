from django.shortcuts import render

# View for the index page
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def property(request):
    return render(request, 'property.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def propertydetail(request):
    return render(request, 'propertydetail.html')