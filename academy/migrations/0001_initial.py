# Generated by Django 3.1.4 on 2021-02-05 03:30

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('exam', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('viewed', models.IntegerField(default=0, null=True)),
                ('test_date', models.DateField(null=True)),
                ('link', models.TextField(null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_pk', models.IntegerField()),
                ('topic', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.FileField(upload_to='documents/class_files')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=64)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to='profiles/')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('subject', models.CharField(choices=[('ph', 'Physics'), ('mt', 'Mathematics'), ('cs', 'Computer Science'), ('bi', 'Biology')], max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('viewed', models.IntegerField(default=0, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=100)),
                ('code', models.TextField()),
            ],
        ),
    ]