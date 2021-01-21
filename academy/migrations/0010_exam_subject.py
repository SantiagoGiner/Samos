# Generated by Django 3.1.4 on 2021-01-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0009_auto_20210119_1741'),
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
                ('comments', models.TextField()),
                ('other_info', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('subject', models.CharField(choices=[('ph', 'Physics'), ('mt', 'Math'), ('cs', 'Computer Science'), ('bi', 'Biology'), ('ch', 'Chemistry')], max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('viewed', models.IntegerField(default=0, null=True)),
                ('comments', models.TextField()),
                ('other_info', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]