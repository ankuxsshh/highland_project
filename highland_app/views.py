# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property

def index(request):
    properties = Property.objects.all()
    return render(request, 'index.html', {'properties': properties})

def about(request):
    return render(request, 'about.html')

def property_view(request):
    properties = Property.objects.all()
    return render(request, 'property.html', {'properties': properties})

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def property_details(request, property_id):  # Ensure this matches the URL pattern
    property_instance = get_object_or_404(Property, pk=property_id)  # Renamed variable for clarity
    return render(request, 'property_details.html', {'property': property_instance})

def property_list(request):
    properties = Property.objects.all()

    # Filtering logic
    property_type = request.GET.getlist('propertyType')
    price_range = request.GET.getlist('priceRange')
    min_sqft = request.GET.getlist('minSqFt')
    bedrooms = request.GET.getlist('bedrooms')

    # Apply filters
    if property_type:
        properties = properties.filter(property_type__in=property_type)

    if price_range:
        if 'under200K' in price_range:
            properties = properties.filter(price__lt=200000)
        if '200Kto500K' in price_range:
            properties = properties.filter(price__gte=200000, price__lt=500000)
        if '500Kto1M' in price_range:
            properties = properties.filter(price__gte=500000, price__lt=1000000)
        if 'over1M' in price_range:
            properties = properties.filter(price__gte=1000000)

    if min_sqft:
        properties = properties.filter(sqft__gte=min(map(int, min_sqft)))

    if bedrooms:
        properties = properties.filter(bedrooms__in=list(map(int, bedrooms)))

    return render(request, 'property.html', {'properties': properties})
