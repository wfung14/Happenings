from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from django.contrib.auth.decorators import login_required

# Define the home view


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'events/index.html')


@login_required
def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {
        'events': events
    })


@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {'event': event})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def about(request):
    return render(request, 'about.html')


