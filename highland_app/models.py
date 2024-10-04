from django.db import models

class Property(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='properties/')
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_sqft = models.IntegerField()
    max_sqft = models.IntegerField()
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
