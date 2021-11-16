from django.db import models
from company_profile.models import Profile

class Services(models.Model):
    name =models.CharField(max_length=120)
    description = models.TextField()#What is the service about and how can it be  accessed
    profile = models.ManyToManyField(Profile)#This is the profile of a company or user interested in a particular service

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Location(models.Model):
    country = models.CharField(max_length=120)
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=120)
    address = models.CharField(max_length=200)#Add the building and the plot number

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
    
    def __str__(self):
        return self.address
    
class Account(models.Model):
    company_name = models.CharField(max_length=250)
    services = models.ManyToManyField(Services, blank=True)
    location = models.ManyToManyField(Location, blank=False)
    contact = models.ManyToManyField(Contact, blank=True)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
            # indexes = [
            #     models.Index(fields=['id', 'slug'])
            # ]

    def __str__(self):
        return self.company_name  
