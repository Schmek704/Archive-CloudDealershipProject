from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=45) 

    def __str__(self):
        return self.name


class CarModel(models.Model):
    model = models.CharField(max_length=30)
    dealer_id = models.IntegerField()    
    name = models.CharField(max_length=30)
    model_type = models.CharField(max_length=20) 
    year = models.DateField()

    def __str__(self):
        return self.name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
