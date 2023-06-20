from django.shortcuts import render, redirect
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
    form = EventForm(request.POST)
    context = {"event_form": event_form}
    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        form.save()
        return redirect("/")
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
