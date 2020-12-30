from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CreateUser(UserCreationForm):
    SUBJECT_CHOICES = [
        ('ph', 'Physics'),
        ('mt', 'Math'),
        ('cs', 'Computer Science'),
        ('bi', 'Biology'),
        ('ch', 'Chemistry'),
    ]
    
    EXAMS_CHOICES = [
        ('sat', 'SAT'),
        ('act', 'ACT'),
        ('toefl', 'TOEFL'),
        ('sat_phys', 'SAT Subject Test: Physics'),
        ('sat_math1', 'SAT Subject Test: Math Level 1'),
        ('sat_math2', 'SAT Subject Test: Math Level 2'),
        ('ap_phys1', 'AP Physics 1'),
        ('ap_phys2', 'AP Physics 2'),
        ('ap_phys_em', 'AP Physics C: Electricity & Magnetism'),
        ('ap_phys_mech', 'AP Physics C: Mechanics'),
    ]
    first_name = forms.CharField(max_length=64, help_text='Enter your first name.')
    last_name = forms.CharField(max_length=64, help_text='Enter your last name.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    subjects = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=SUBJECT_CHOICES,
        help_text='''What subject areas are you interested in studying? If interested in 
                    another subject, include it in the comments section below''', 
    )
    exams = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=EXAMS_CHOICES,
        help_text='''Are there any exams you want to study for? If planning on taking another exam, 
                    include it in comments below''',
        required=False
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea,
        help_text='Any general comments?'
    )
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 
                   'subjects', 'exams',)