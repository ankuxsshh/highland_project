from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('about', views.about, name='about'),  
    path('services', views.services, name='services'),
    path('property', views.property, name='property'),
    path('contact', views.contact, name='contact'),
    path('propertydetail', views.propertydetail, name='propertydetail'),
]