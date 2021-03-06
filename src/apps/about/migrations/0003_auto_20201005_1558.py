# Generated by Django 3.0.10 on 2020-10-05 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('about', '0002_aboutpage_sub_banner_angle_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='sub_banner_angle_img',
            field=models.ForeignKey(help_text='Мелкаий треугольник возле главного банера', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='about_sub_banner_angle_img', to='wagtailimages.Image'),
        ),
    ]
