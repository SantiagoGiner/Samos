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
from .models import *


SUBJECT_CHOICES = ['ph', 'mt', 'cs', 'bi']

EXAMS_CHOICES = [ 
    'sat', 'act', 'toefl', 'ielts','ap_phys1', 
    'ap_phys2', 'ap_phys_em','ap_phys_mech'
]
    

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
    if Subject.objects.filter(user_id=request.user.pk) or Exam.objects.filter(user_id=request.user.pk):
        return HttpResponseRedirect(reverse('academy:classes'))
    return render(request, 'academy/about.html', {
        'message': '''**Looks like you haven't enrolled in any classes. '''
    })


@login_required
@object_required
def about(request):
    return render(request, 'academy/about.html')


@login_required
@object_required
def change_profile(request, profile_id, action):
    if request.method == 'POST':
        if action == 'delete':
            Profile.objects.get(pk=profile_id).delete()
            messages.success(request, 'You have deleted your profile.')
        elif action == 'update':
            profile = Profile.objects.get(pk=profile_id)
            profile.country = request.POST['country']
            profile.city = request.POST['city']
            profile.bio = request.POST['bio']
            profile.photo = request.FILES['photo']
            profile.save()
            messages.success(request, 'Profile successfully updated!')
        else:
            messages.warning(request, f'The action {action} is invalid.')
        return HttpResponseRedirect(reverse('academy:profile'))

@login_required
@object_required
def classes(request):
    subjects = Subject.objects.filter(user_id=request.user.pk)
    exams = Exam.objects.filter(user_id=request.user.pk)
    return render(request, 'academy/classes.html', {
        'subjects': subjects,
        'exams': exams
    })


@login_required
def enroll(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            new_subjects = form.cleaned_data['subjects']
            new_exam = form.cleaned_data['exam']
            if len(new_subjects) != 0 or new_exam != '':
                for subject in new_subjects:
                    if Subject.objects.filter(user_id=request.user.pk, subject=subject):
                        messages.warning(request, 'You have already enrolled in all or some of the subjects chosen.')
                        return HttpResponseRedirect(reverse('academy:enroll'))
                    elif subject not in SUBJECT_CHOICES:
                        messages.warning(request, 'That is not a valid subject.')
                        return HttpResponseRedirect(reverse('academy:enroll'))
                    Subject(
                        user_id=request.user.pk,
                        subject=subject,
                        comments=form.cleaned_data['comments'],
                    ).save()
                if Exam.objects.filter(user_id=request.user.pk, exam=new_exam):
                    messages.warning(request, 'You have already enrolled in all or some of the exams chosen.')
                    return HttpResponseRedirect(reverse('academy:enroll'))
                if new_exam != '':
                    if new_exam not in EXAMS_CHOICES:
                        messages.warning(request, 'That is not a valid exam.')
                        return HttpResponseRedirect(reverse('academy:enroll'))
                    Exam(
                        user_id=request.user.pk,
                        exam=new_exam,
                        test_date=form.cleaned_data['test_date'],
                        comments=form.cleaned_data['comments']
                    ).save()
                messages.success(request, '''You've enrolled! I will reach out to you with further details.''')
                return HttpResponseRedirect(reverse('academy:classes'))
            messages.warning(request, 'Please fill out the form.')
            return HttpResponseRedirect(reverse('academy:enroll'))
                
    return render(request, 'academy/enroll.html', {
        'form': EnrollForm()
    })    


@login_required
def gallery(request):
    return render(request, 'academy/gallery.html', {
        'videos': Video.objects.all()
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
            messages.warning(request, 'Invalid credentials, please try again.')
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


@login_required
def profile(request):
    if request.method == 'POST':
        Profile(
            user_id=request.user.pk,
            country=request.POST['country'],
            city=request.POST['city'],
            bio=request.POST['bio'],
            photo=request.FILES['photo'],
        ).save()
        messages.success(request, 'You have successfully created your profile!')
        return HttpResponseRedirect(reverse('academy:profile'))
    try:
        profile = Profile.objects.get(user_id=request.user.pk)
        return render(request, 'academy/profile.html', {
        'profile': profile,
        'update_profile_form': ProfileForm({
            'country': profile.country, 
            'city': profile.city, 
            'bio': profile.bio,
            'photo': profile.photo
        })
    })
    except ObjectDoesNotExist:
        return render(request, 'academy/profile.html', {
            'add_profile_form': ProfileForm()
        })


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
            messages.success(request, 'You have successfully registered!')
            return HttpResponseRedirect(reverse('academy:index'))
        messages.warning(request, 
                         'Verify that you meet all of the requirements in each field.')
        return HttpResponseRedirect(reverse('academy:register'))
    return render(request, 'academy/register.html', {
        'form': CreateUserForm()
    })

@login_required
def schedule(request):
    return render(request, 'academy/schedule.html')


@login_required
@object_required
def view_class(request, class_type, class_id):
    if request.method == 'POST':
        if class_type == 'Subject':
            Subject.objects.get(pk=class_id).delete()
        elif class_type == 'Exam':
            Exam.objects.get(pk=class_id).delete()
        else:
            messages.warning(request, 'Invalid class type. Please try again.')
            return HttpResponseRedirect(reverse('academy:classes'))
        messages.success(request, 'You have successfully dropped the class.')
        return HttpResponseRedirect(reverse('academy:classes'))

    if class_type == 'Subject':
        return render(request, 'academy/view_class.html', {
            'class': Subject.objects.get(pk=class_id),
            'class_type': 'Subject',
            'files': File.objects.filter(class_id=class_id)
        })
    return render(request, 'academy/view_class.html', {
            'class': Exam.objects.get(pk=class_id),
            'class_type': 'Exam',
            'files': File.objects.filter(class_id=class_id)
        })
