from django.shortcuts import render

# View for the index page
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def properties(request):
    return render(request, 'properties.html')

def services(request):
    return render(request, 'services.html')