from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('description', 'price', 'location', 'property_type')
    search_fields = ('description', 'location')
    list_filter = ('property_type', 'bedrooms')

    # Customize the form if needed
    fieldsets = (
        (None, {
            'fields': ('description', 'image', 'location', 'property_type')
        }),
        ('Price Information', {
            'fields': ('price', 'min_sqft', 'max_sqft', 'min_price', 'max_price', 'bedrooms')
        }),
    )
