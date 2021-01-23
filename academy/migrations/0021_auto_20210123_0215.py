# Generated by Django 3.1.4 on 2021-01-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0020_exam_profile_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(choices=[('ph', 'Physics'), ('mt', 'Math'), ('cs', 'Computer Science'), ('bi', 'Biology')], max_length=20),
        ),
    ]
