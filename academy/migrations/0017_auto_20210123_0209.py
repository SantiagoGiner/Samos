# Generated by Django 3.1.4 on 2021-01-23 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0016_auto_20210121_1527'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]