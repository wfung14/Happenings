from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vendors_detail', kwargs={'pk': self.id})


class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField('Event Date')
    type_event = models.CharField(max_length=100)
    vendors = models.ManyToManyField(Vendor)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'



