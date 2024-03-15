# Generated by Django 5.0.2 on 2024-03-15 06:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_short_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='short_bio',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(256)]),
        ),
    ]