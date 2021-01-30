# Generated by Django 3.1.4 on 2021-01-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0026_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
                ('width', models.CharField(max_length=64)),
                ('height', models.CharField(max_length=64)),
            ],
        ),
    ]