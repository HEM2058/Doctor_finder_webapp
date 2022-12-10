from django.db import models

# Create your models here.

class Doctor(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=50)
    highest_degree = models.CharField(max_length=50)
    services_offers  = models.CharField(max_length=250)
    district = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    is_active = models.BooleanField(default=True)


    def __str(self):
        return self.fname

