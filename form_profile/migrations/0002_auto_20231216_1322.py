# Generated by Django 3.2 on 2023-12-16 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_color',
            field=models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator('^[0-9a-f]{8}$')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
