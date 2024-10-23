# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from django.db.models import Q

def index(request):
    properties = Property.objects.all()
    return render(request, 'index.html', {'properties': properties})

def about(request):
    return render(request, 'about.html')

def property(request):
    properties = Property.objects.all()
    return render(request, 'property.html', {'properties': properties})

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def property_details(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    additional_images = []
    for i in range(1, 11):
        img_field = getattr(property, f"additional_images{i}", None)
        if img_field:
            additional_images.append(img_field.url)

    return render(request, 'property_details.html', {
        'property': property,
        'additional_images': additional_images,
    })

def property_list(request):
    properties = Property.objects.all()  # Fetch all properties initially

    # Retrieve query parameters from GET request
    location_query = request.GET.get('location', '').strip()
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_sqft = request.GET.get('min_sqft')
    max_sqft = request.GET.get('max_sqft')
    property_type = request.GET.getlist('property_type')
    bedrooms = request.GET.getlist('bedrooms')

    # Filter by location if provided
    if location_query:
        properties = properties.filter(property_location__icontains=location_query)

    # Filter by minimum and maximum price
    if min_price:
        if int(min_price) == 10000001:
            properties = properties.filter(property_price__gt=10000000)
        else:
            properties = properties.filter(property_price__gte=int(min_price))

    if max_price and int(max_price) != 10000001:
        properties = properties.filter(property_price__lte=int(max_price))

    # Filter by square feet
    if min_sqft:
        properties = properties.filter(square_feet__gte=int(min_sqft))
    if max_sqft:
        properties = properties.filter(square_feet__lte=int(max_sqft))

    # Filter by property type if selected
    if property_type:
        properties = properties.filter(property_type__in=property_type)

    # Filter by bedrooms
    if bedrooms:
        bedrooms = [int(bedroom) for bedroom in bedrooms]
        if 5 in bedrooms:
            properties = properties.filter(bedrooms__gte=5)
        else:
            properties = properties.filter(bedrooms__in=bedrooms)

    return render(request, 'property.html', {
        'properties': properties,
        'location_query': location_query,
        'min_price': min_price,
        'max_price': max_price,
        'min_sqft': min_sqft,
        'max_sqft': max_sqft,
        'property_type': property_type,
        'bedrooms': bedrooms,
    })