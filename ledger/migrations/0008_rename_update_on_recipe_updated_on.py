# Generated by Django 5.0.2 on 2024-03-15 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0007_alter_recipe_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='update_on',
            new_name='updated_on',
        ),
    ]
