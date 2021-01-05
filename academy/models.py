from django import forms
from django.db import models


class subjects(models.Model):
    user_id = models.IntegerField()
    subject = models.CharField(max_length=20)
    # TODO: Insert field for files, e.g. pdf's, recordings, etc.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Order the subject by date added
    class Meta:
        ordering = ('-created',)


class exams(models.Model):
    user_id = models.IntegerField()
    exam = models.CharField(max_length=20)
    deadline = models.DateField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Order the subject by date added
    class Meta:
        ordering = ('-created',)