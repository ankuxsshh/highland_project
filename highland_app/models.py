# models.py
from django.db import models

class Property(models.Model):
    name = models.TextField(default="Unnamed Property")
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=[
        ('Single Family Home', 'Single Family Home'),
        ('Apartment', 'Apartment'),
        ('Commercial', 'Commercial'),
        ('Land', 'Land'),
        ('Multi-Family', 'Multi-Family')
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sqft = models.IntegerField()
    bedrooms = models.IntegerField()
    description = models.TextField()

    # Add features
    wifi = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.location} - ${self.price}"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.property.name}"
