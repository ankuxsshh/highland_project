# admin.py
from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1  # Allows for adding one extra image

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location', 'property_type', 'bedrooms', 'sqft')
    search_fields = ('name', 'location')
    list_filter = ('property_type', 'bedrooms', 'price', 'sqft')
    inlines = [PropertyImageInline]  # Enables image uploads in the property form

    fieldsets = (
        (None, {
            'fields': ('name', 'location', 'property_type')
        }),
        ('Details', {
            'fields': ('price', 'sqft', 'bedrooms', 'description', 'wifi', 'pool', 'parking', 'garden')
        }),
    )

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image')
