from django.db import models
 
class Profile(models.Model):#Think of adding an initial
    full_name = models.CharField(max_length=200)
    country = models.CharField(max_length=180)
    company = models.CharField(max_length=128, null=True)
    phone_no = models.CharField(max_length=120, default='+000 000000000')
    address = models.CharField(max_length=200)#Company address
    email = models.EmailField()

    def __str__(self):
        return self.full_name
