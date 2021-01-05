from functools import wraps

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages

from .forms import *


# Decorator that handles exception if an object is not found in the database
def object_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        # If object requested is not found, redirect user and inform them so
        except ObjectDoesNotExist:
            messages.warning(args[0], 'Seems like that element requested does not exist. Please try again.')
            return HttpResponseRedirect(reverse('academy:index'))
    return decorated_function


@login_required
def index(request):
    return render(request, 'academy/index.html')


@login_required
@object_required
def classes(request):
    return render(request, 'academy/classes.html')


@login_required
def enroll(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        messages.success(request, '''You've enrolled! I will reach out to you with further details''')
        return HttpResponseRedirect(reverse('academy:enroll'))
    return render(request, 'academy/enroll.html', {
        'form': EnrollForm()
    })    


def login_view(request):
    # Route was reached via POST, as by submitting a form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Validate that the user input a correct username and password
        user = authenticate(request, username=username, password=password)
        # If so, log the user in
        if user is not None:
            login(request, user)
            messages.success(request, f'Logged in as {request.user.username}!')
            return HttpResponseRedirect(reverse('academy:index'))
        # Else, redirect them to the login page again, informing them of the error
        else:
            messages.warning(request, 'Invalid credentials')
            return render(request, 'academy/login.html', {
                'form': AuthenticationForm()
            })

    # Else, user reached via GET, as by clicking a link
    return render(request, 'academy/login.html', {
        'form': AuthenticationForm()
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out!')
    return HttpResponseRedirect(reverse('academy:login'))


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Add the user to the users table
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log the user in
            new_user = authenticate(request, username=username, password=password)
            login(request, new_user)
            messages.success(request, 'Registered!')
            return HttpResponseRedirect(reverse('academy:index'))
        messages.warning(request, 
                         'Verify that you meet all of the requirements in each field!')
        return HttpResponseRedirect(reverse('academy:register'))
    return render(request, 'academy/register.html', {
        'form': CreateUserForm()
    })

@login_required
def schedule(request):
    return render(request, 'academy/schedule.html')