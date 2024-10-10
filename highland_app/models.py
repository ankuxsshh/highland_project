# models.py
from django.db import models

class Property(models.Model):
    property_name = models.TextField(default="")
    property_location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=[
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment'),
        ('Studio Flat', 'Studio Flat'),
    ])
    property_price = models.TextField(default="")
    square_feet = models.IntegerField()
    bedrooms = models.IntegerField()
    property_description = models.TextField()

    # Features
    wifi = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    car_parking = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)

    # Images
    main_image = models.ImageField(upload_to='property_images/', blank=True, null=True)  # Main image
    additional_images1 = models.ImageField(upload_to='property_images/', blank=True, null=True)  
    additional_images2 = models.ImageField(upload_to='property_images/', blank=True, null=True)  
    additional_images3 = models.ImageField(upload_to='property_images/', blank=True, null=True)  
    additional_images4 = models.ImageField(upload_to='property_images/', blank=True, null=True)  

    def __str__(self):
        return f"{self.property_name} - {self.property_location} - ${self.property_price}"
