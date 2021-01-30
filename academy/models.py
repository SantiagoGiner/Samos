from django import forms
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class Subject(models.Model):
    SUBJECT_CHOICES = [
        ('ph', 'Physics'),
        ('mt', 'Math'),
        ('cs', 'Computer Science'),
        ('bi', 'Biology'),
    ]

    user_id = models.IntegerField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    date = models.DateField(auto_now_add=True)
    viewed = models.IntegerField(null=True, default=0)
    link = models.TextField(null=True, blank=True)
    files = models.FileField(upload_to='documents/class_files', null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Order the subject by date added
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.subject == 'ph':
            return 'Physics'
        elif self.subject == 'mt':
            return 'Mathematics'
        elif self.subject == 'cs':
            return 'Computer Science'
        elif self.subject == 'bi':
            return 'Biology'
        elif self.subject == 'ch':
            return 'Chemistry'
        else:
            return self.subject

class Exam(models.Model):
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

    user_id = models.IntegerField()
    exam = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    viewed = models.IntegerField(null=True, default=0)
    test_date = models.DateField(null=True)
    link = models.TextField(null=True)
    files = models.FileField(upload_to='documents/class_files', null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Order the subject by date added
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        if self.exam in ['sat', 'act','toefl', 'ielts']:
            return self.exam.upper()
        elif self.exam == 'ap_phys1':
            return 'AP Physics 1'
        elif self.exam == 'ap_phys2':
            return 'AP Physics 2'
        elif self.exam == 'ap_phys_em':
            return 'AP Physics C: Electricity & Magnetism'
        elif self.exam == 'ap_phys_mech':
            return 'AP Physics C: Mechanics'
        else:
            return self.exam


class Profile(models.Model):
    user_id = models.IntegerField()
    country = CountryField()
    city = models.CharField(max_length=64)
    bio = models.TextField()
    photo = models.ImageField(null=True, upload_to='profiles/')


class Video(models.Model):
    tagline = models.CharField(max_length=64)
    title = models.CharField(max_length=100)
    code = models.TextField()
