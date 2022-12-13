from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=5000)
    bio = models.TextField()
    phone = models.CharField(max_length=15, null=True)
    company = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True, null=True)
    photo = models.ImageField(null=True, blank=False, upload_to='media/agents')

    class Meta:
        ordering = [ '-created']

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name



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
    town = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    floor_plan = models.ImageField(upload_to='media')
    price = models.FloatField()
    property_type = models.CharField(max_length=50, choices=STATUS)
    year_built = models.IntegerField()
    contract_type = models.CharField(max_length=50, choices=C_STATUS)
    home_area = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms =  models.IntegerField()
    parking = models.IntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title

class Photo(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    photos = models.ImageField(null=True, blank=False, upload_to='media')



class Property_review(models.Model):
    creator = models.CharField(max_length=500, null=True)
    body = models.TextField(null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)