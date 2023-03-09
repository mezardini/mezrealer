from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Property(models.Model):
    APARTMENT = 'apartment'
    BUNGALOW = 'bungalow'
    DUPLEX = 'duplex'
    STATUS = [
       (APARTMENT, ('Apartment')),
       (BUNGALOW, ('Bungalow')),
       (DUPLEX, ('Duplex')),
   ]
    RENT = 'rent'
    SALE = 'sale'
    C_STATUS = [
       (RENT, ('Rent')),
       (SALE   , ('Sale')),
    ]
    title = models.CharField(max_length=5000)
    description = models.TextField()
    address = models.CharField(max_length=5000)
    floor_plan = models.ImageField(upload_to='media')
    price = models.FloatField()
    property_type = models.CharField(max_length=50, choices=STATUS)
    year_of_build = models.DateField(blank=True, null=True)
    contract_type = models.CharField(max_length=50, choices=C_STATUS)
    home_area = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms =  models.IntegerField()
    parking = models.IntegerField(null=True)
    agent_name = models.CharField(max_length=100, null=True)
    agent_mail = models.CharField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title

class Photo(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    photos = models.ImageField(null=True, blank=False, upload_to='media')





