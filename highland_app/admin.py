# admin.py
from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'property_price', 'property_location', 'property_type', 'bedrooms', 'square_feet')
    search_fields = ('property_name', 'property_location')
    list_filter = ('property_type', 'bedrooms', 'property_price', 'square_feet')

    fieldsets = (
        (None, {
            'fields': ('property_name', 'property_location', 'property_type', 'main_image', 'additional_images1', 'additional_images2', 'additional_images3', 'additional_images4')
        }),
        ('Details', {
            'fields': ('property_price', 'square_feet', 'bedrooms', 'property_description', 'wifi', 'swimming_pool', 'car_parking', 'garden')
        }),
    )
