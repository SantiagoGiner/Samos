# Generated by Django 3.1.4 on 2021-01-27 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0022_auto_20210127_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='files',
            field=models.FileField(null=True, upload_to='documents/class_files'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='files',
            field=models.FileField(null=True, upload_to='documents/class_files'),
        ),
    ]
