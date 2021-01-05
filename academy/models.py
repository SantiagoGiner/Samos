from django.db import models


# Declare an input class that accepts a date
class DateInput(forms.DateInput):
    input_type = 'date'


class subjects(models.Model):
    user_id = models.IntegerField()
    subject = models.CharField(max_length=20)
    # Insert field for files, e.g. pdf's, recordings, etc.


class exams(models.Model):
    user_id = models.IntegerField()
    exam = models.CharField(max_length=20)
    deadline = forms.DateField(help_text='What is the date of the exam?', 
                                widget=DateInput())