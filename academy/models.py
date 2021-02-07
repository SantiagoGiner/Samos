from django.conf import settings
from django import forms
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.contrib import admin


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

class Subject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    date = models.DateField(auto_now_add=True)
    viewed = models.IntegerField(null=True, default=0)
    link = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Order the subject by date added
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        subjects = {}
        for subject in SUBJECT_CHOICES:
            subjects[subject[0]] = subject[1]
        return self.user.get_full_name() + ' - ' + subjects[self.subject]


class SubjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Exam(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exam = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    viewed = models.IntegerField(null=True, default=0)
    test_date = models.DateField(null=True)
    link = models.TextField(null=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Order the subject by date added
    class Meta:
        ordering = ('-created',)


    def __str__(self):
        exams = {}
        for exam in EXAMS_CHOICES:
            exams[exam[0]] = exam[1]
        return self.user.get_full_name() + ' - ' + exams[self.exam]


class ExamAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Profile(models.Model):
    user_id = models.IntegerField()
    country = CountryField()
    city = models.CharField(max_length=64)
    bio = models.TextField()
    photo = models.ImageField(null=True, upload_to='profiles/')


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Video(models.Model):
    tagline = models.CharField(max_length=64)
    title = models.CharField(max_length=100)
    code = models.TextField()

    def __str__(self):
        return self.title


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class File(models.Model):
    class_id = models.IntegerField()
    topic = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    content = models.FileField(upload_to='documents/class_files')

    def __str__(self):
        return self.title


class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
