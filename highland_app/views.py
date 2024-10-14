# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from django.db.models import Q
from functools import reduce
from operator import or_

def index(request):
    properties = Property.objects.all()
    return render(request, 'index.html', {'properties': properties})

def about(request):
    return render(request, 'about.html')

def property(request):
    properties = Property.objects.all()
    properties = Property.objects.all()  # Start with all properties

    # Get the search query for location from the search bar
    location_query = request.GET.get('location', '')  # Capture location search query from GET request

    # Filter properties by location if a location query is provided
    if location_query:
        properties = properties.filter(property_location__icontains=location_query)

    # Additional filters for property type, price, square feet, bedrooms (already in place)
    selected_property_type = request.GET.getlist('property_type')
    selected_price_range = request.GET.getlist('property_price')
    selected_square_feet = request.GET.getlist('square_feet')
    selected_bedrooms = request.GET.getlist('bedrooms')

    if selected_property_type:
        properties = properties.filter(property_type__in=selected_property_type)

    if selected_price_range:
        price_mapping = {
            'Under 5L.': (0, 500000),
            '5L. - 10L.': (500000, 1000000),
            '10L. - 25L.': (1000000, 2500000),
            '25L. - 50L.': (2500000, 5000000),
            '50L. - 75L.': (5000000, 7500000),
            '75L. - 1Cr.': (7500000, 10000000),
            'Above 1Cr.': (10000000, 1000000000),
        }
        filters = [Q(property_price__gte=price_mapping[pr][0], property_price__lte=price_mapping[pr][1]) for pr in selected_price_range if pr in price_mapping]
        if filters:
            properties = properties.filter(reduce(or_, filters))

    if selected_square_feet:
        square_feet_mapping = {
            'Under 500 sq.ft': (0, 500),
            '500 - 1000 sq.ft': (500, 1000),
            '1000 - 1500 sq.ft': (1000, 1500),
            '1500 - 2000 sq.ft': (1500, 2000),
            '2000 - 2500 sq.ft': (2000, 2500),
            '2500 - 3000 sq.ft': (2500, 3000),
        }
        filters = [Q(square_feet__gte=square_feet_mapping[sf][0], square_feet__lte=square_feet_mapping[sf][1]) for sf in selected_square_feet if sf in square_feet_mapping]
        if filters:
            properties = properties.filter(reduce(or_, filters))

    # Handle the bedrooms filter with the special case for "5+"
    if selected_bedrooms:
        bedroom_filters = Q()
        for bedroom in selected_bedrooms:
            if bedroom == '5+':
                bedroom_filters |= Q(bedrooms__gte=5)  # Handle 5+ case
            else:
                bedroom_filters |= Q(bedrooms=bedroom)  # Exact match for other cases
        properties = properties.filter(bedroom_filters)

    # Render filtered properties in property.html template
    return render(request, 'property.html', {
        'properties': properties,  # Pass filtered properties
        'property_types': ['Villa', 'Apartment', 'Studio Flat'],
        'price_ranges': ['Under 5L.', '5L. - 10L.', '10L. - 25L.', '25L. - 50L.', '50L. - 75L.', '75L. - 1Cr.', 'Above 1Cr.'],
        'square_feet_options': ['Under 500 sq.ft', '500 - 1000 sq.ft', '1000 - 1500 sq.ft', '1500 - 2000 sq.ft', '2000 - 2500 sq.ft', '2500 - 3000 sq.ft'],
        'bedroom_options': ['1', '2', '3', '4', '5', '5+'],
        'selected_location': location_query,  # Pass selected location to the template to keep the search field filled
        'selected_property_type': selected_property_type,
        'selected_price_range': selected_price_range,
        'selected_square_feet': selected_square_feet,
        'selected_bedrooms': selected_bedrooms,
    })


def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def property_details(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    # Create a list of additional image URLs
    additional_images = []
    for i in range(1, 11):
        img_field = getattr(property, f"additional_images{i}", None)
        if img_field:
            additional_images.append(img_field.url)

    return render(request, 'property_details.html', {
        'property': property,
        'additional_images': additional_images,  # Pass list of image URLs to the template
    })


def property_list(request):
    properties = Property.objects.all()  # Start with all properties

    # Get the search query for location from the search bar
    location_query = request.GET.get('location', '')  # Capture location search query from GET request

    # Filter properties by location if a location query is provided
    if location_query:
        properties = properties.filter(property_location__icontains=location_query)

    # Additional filters for property type, price, square feet, bedrooms (already in place)
    selected_property_type = request.GET.getlist('property_type')
    selected_price_range = request.GET.getlist('property_price')
    selected_square_feet = request.GET.getlist('square_feet')
    selected_bedrooms = request.GET.getlist('bedrooms')

    if selected_property_type:
        properties = properties.filter(property_type__in=selected_property_type)

    if selected_price_range:
        price_mapping = {
            'Under 5L.': (0, 500000),
            '5L. - 10L.': (500000, 1000000),
            '10L. - 25L.': (1000000, 2500000),
            '25L. - 50L.': (2500000, 5000000),
            '50L. - 75L.': (5000000, 7500000),
            '75L. - 1Cr.': (7500000, 10000000),
            'Above 1Cr.': (10000000, 1000000000),
        }
        filters = [Q(property_price__gte=price_mapping[pr][0], property_price__lte=price_mapping[pr][1]) for pr in selected_price_range if pr in price_mapping]
        if filters:
            properties = properties.filter(reduce(or_, filters))

    if selected_square_feet:
        square_feet_mapping = {
            'Under 500 sq.ft': (0, 500),
            '500 - 1000 sq.ft': (500, 1000),
            '1000 - 1500 sq.ft': (1000, 1500),
            '1500 - 2000 sq.ft': (1500, 2000),
            '2000 - 2500 sq.ft': (2000, 2500),
            '2500 - 3000 sq.ft': (2500, 3000),
        }
        filters = [Q(square_feet__gte=square_feet_mapping[sf][0], square_feet__lte=square_feet_mapping[sf][1]) for sf in selected_square_feet if sf in square_feet_mapping]
        if filters:
            properties = properties.filter(reduce(or_, filters))

    # Handle the bedrooms filter with the special case for "5+"
    if selected_bedrooms:
        bedroom_filters = Q()
        for bedroom in selected_bedrooms:
            if bedroom == '5+':
                bedroom_filters |= Q(bedrooms__gte=5)  # Handle 5+ case
            else:
                bedroom_filters |= Q(bedrooms=bedroom)  # Exact match for other cases
        properties = properties.filter(bedroom_filters)

    # Render filtered properties in property.html template
    return render(request, 'property.html', {
        'properties': properties,  # Pass filtered properties
        'property_types': ['Villa', 'Apartment', 'Studio Flat'],
        'price_ranges': ['Under 5L.', '5L. - 10L.', '10L. - 25L.', '25L. - 50L.', '50L. - 75L.', '75L. - 1Cr.', 'Above 1Cr.'],
        'square_feet_options': ['Under 500 sq.ft', '500 - 1000 sq.ft', '1000 - 1500 sq.ft', '1500 - 2000 sq.ft', '2000 - 2500 sq.ft', '2500 - 3000 sq.ft'],
        'bedroom_options': ['1', '2', '3', '4', '5', '5+'],
        'selected_location': location_query,  # Pass selected location to the template to keep the search field filled
        'selected_property_type': selected_property_type,
        'selected_price_range': selected_price_range,
        'selected_square_feet': selected_square_feet,
        'selected_bedrooms': selected_bedrooms,
    })