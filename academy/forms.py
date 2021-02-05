from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_countries.fields import CountryField


# Declare an input class that accepts a date
class DateTimeInput(forms.DateInput):
    input_type = 'date'


# Modify the Django UserCreationForm so as to include first name, last name, and email
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=64, help_text='Enter your first name.')
    last_name = forms.CharField(max_length=64, help_text='Enter your last name.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EnrollForm(forms.Form):
    SUBJECT_CHOICES = [
        ('ph', 'Physics'),
        ('mt', 'Mathematics'),
        ('cs', 'Computer Science'),
    ]
    EXAMS_CHOICES = [
        ('sat', 'SAT'),
        ('act', 'ACT'),
        ('toefl', 'TOEFL'),
        ('ielts', 'IELTS'),
        ('ap_phys1', 'AP Physics 1'),
        ('ap_phys2', 'AP Physics 2'),
        ('ap_phys_em', 'AP Physics C: Electricity & Magnetism'),
        ('ap_phys_mech', 'AP Physics C: Mechanics'),
    ]
    subjects = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=SUBJECT_CHOICES,
        help_text='''What subject areas are you interested in studying? If interested in 
                    another subject, include it in the comments section below.''', 
    )
    exam = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EXAMS_CHOICES,
        help_text='''Are there any exams you want to study for? If planning on taking another exam, 
                    include it in comments below.''',
    )
    test_date = forms.DateTimeField(
        required=False,
        help_text='What is the date of the exam?', 
        widget=DateTimeInput(),
    )
    '''availability = forms.DateTimeField(
        widget=DateTimeInput(),
        help_text='Days and times at which you are available to attend tutoring sessions'
        )'''
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea,
        help_text='''Any general comments (e.g. what specific 
                     topics are you interested in for the subjects chosen above)?'''
    )


class ProfileForm(forms.Form):
    country = CountryField().formfield(
        help_text='What is your country of origin?',
        blank_label='Select country'
    )
    city = forms.CharField(max_length=64, help_text='What is your city of origin?')
    bio = forms.CharField(
        widget=forms.Textarea,
        help_text='''Tell us about yourself. Provide a brief description of interests, hobbies, goals, 
                      or anything else you may want to add.'''
    )
    photo = forms.ImageField(help_text='If you want to, submit a photo of yourself.')
    
class ManageAccountForm(forms.Form):
    username = forms.CharField(max_length=64)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
