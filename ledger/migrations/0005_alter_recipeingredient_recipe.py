# Generated by Django 5.0.2 on 2024-03-04 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_alter_recipeingredient_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='ledger.recipe'),
        ),
    ]
