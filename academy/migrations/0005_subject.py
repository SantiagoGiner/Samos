# Generated by Django 3.1.4 on 2021-02-07 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0004_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('ph', 'Physics'), ('mt', 'Mathematics'), ('cs', 'Computer Science')], max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('viewed', models.IntegerField(default=0, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]