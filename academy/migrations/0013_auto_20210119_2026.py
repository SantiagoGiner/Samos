# Generated by Django 3.1.4 on 2021-01-19 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0012_exam_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='image',
        ),
    ]