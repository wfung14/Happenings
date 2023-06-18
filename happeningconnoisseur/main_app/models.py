from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField('Event Date')
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # food = models.CharField(max_length=250)
    # drinks = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vendors_detail', kwargs={'pk': self.id})
