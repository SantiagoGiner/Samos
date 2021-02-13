from django.conf import settings
from django import forms
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.contrib import admin


COURSE_CHOICES = [
    ('ph', 'Physics'),
    ('mt', 'Mathematics'),
    ('cs', 'Computer Science'),
    ('sat', 'SAT'),
    ('act', 'ACT'),
    ('toefl', 'TOEFL'),
    ('ielts', 'IELTS'),
    ('ap_phys1', 'AP Physics 1'),
    ('ap_phys2', 'AP Physics 2'),
    ('ap_phys_em', 'AP Physics C: Electricity & Magnetism'),
    ('ap_phys_mech', 'AP Physics C: Mechanics'),
]

COURSES = {}
for course in COURSE_CHOICES:
    COURSES[course[0]] = course[1]


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, null=True, choices=COURSE_CHOICES)
    date = models.DateField(auto_now_add=True)
    viewed = models.IntegerField(null=True, default=0)
    test_date = models.DateField(null=True)
    link = models.TextField(null=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Order the subject by date added
    class Meta:
        ordering = ('-created',)

    def user_course_name(self):
        return self.user.get_full_name() + ' - ' + COURSES[self.code]

    def __str__(self):
        return COURSES[self.code]


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('user_course_name',)
        return ('__str__',)


class File(models.Model):
    course_id = models.IntegerField()
    topic = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    content = models.FileField(upload_to='documents/class_files')

    def __str__(self):
        return self.title


class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, upload_to='profiles/', blank=True)

    def __str__(self):
        return self.user.get_full_name()

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)


class Video(models.Model):
    tagline = models.CharField(max_length=64)
    title = models.CharField(max_length=100)
    code = models.TextField()

    def __str__(self):
        return self.title


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)
