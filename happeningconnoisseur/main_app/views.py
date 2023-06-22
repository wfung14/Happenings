import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Vendor
from django.contrib.auth.decorators import login_required
from .forms import EventForm


def events_index(request):
    events = Event.objects.all()
    return render(request, "events/index.html", {"events": events})


@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    vendors = event.vendors.all().values_list("id")
    all_vendors = Vendor.objects.exclude(id__in=vendors)
    context = {"event": event, "all_vendors": all_vendors}
    return render(request, "events/detail.html", context)


@login_required
def events_add(request):
    event_form = EventForm()
    context = {"event_form": event_form}
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            
            Event.objects.create(photo=url, name=list(request.POST.values())[1], location=list(request.POST.values())[2], date=list(request.POST.values())[3], type_event=list(request.POST.values())[4], user=request.user)
            
            return redirect("/")
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return render(request, "events/add.html", context)


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect("index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


def about(request):
    return render(request, "about.html")


@login_required
def vendors_index(request):
    vendors = Vendor.objects.all()
    context = {"vendors": vendors}
    return render(request, "vendors/index.html", context)


@login_required
def assoc_vendor(request, event_id, vendor_id):
    Event.objects.get(id=event_id).vendors.add(vendor_id)
    return redirect("detail", event_id=event_id)


@login_required
def unassoc_vendor(request, event_id, vendor_id):
    Event.objects.get(id=event_id).vendors.remove(vendor_id)
    return redirect("detail", event_id=event_id)


class EventDelete(DeleteView):
    model = Event
    success_url = "/"


class EventUpdate(UpdateView):
    model = Event
    fields = ["name", "location", "date", "type_event"]
