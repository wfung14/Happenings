from django.db import models

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  date = models.DateField('Event Date')
  type = models.CharField(max_length=100)