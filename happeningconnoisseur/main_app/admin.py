from django.contrib import admin
# import your models here
from .models import Event, Vendor

# Register your models here
admin.site.register(Event)
admin.site.register(Vendor)