# Generated by Django 3.1.4 on 2021-01-27 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0023_auto_20210127_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='documents/class_files'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='documents/class_files'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
    ]