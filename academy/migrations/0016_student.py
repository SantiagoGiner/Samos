# Generated by Django 3.1.6 on 2021-02-11 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0015_auto_20210210_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('city', models.CharField(max_length=64, null=True)),
                ('bio', models.TextField(null=True)),
                ('photo', models.ImageField(null=True, upload_to='profiles/')),
                ('courses', models.ManyToManyField(to='academy.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
