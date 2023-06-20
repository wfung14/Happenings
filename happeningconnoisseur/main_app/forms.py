from django.forms import ModelForm
from .models import Event, Vendor


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "location", "date", "type_event"]
