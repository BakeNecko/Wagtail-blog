# Generated by Django 3.0.10 on 2020-10-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0009_auto_20201004_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpostpage',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='blogpostpage',
            name='external_page',
        ),
        migrations.RemoveField(
            model_name='blogpostpage',
            name='internal_page',
        ),
        migrations.AddField(
            model_name='blogpostpage',
            name='post_title',
            field=models.CharField(default=None, max_length=155, null=True),
        ),
    ]
