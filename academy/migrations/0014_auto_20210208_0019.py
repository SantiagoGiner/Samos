# Generated by Django 3.1.6 on 2021-02-08 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0013_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='class_id',
            new_name='course_id',
        ),
    ]