# Generated by Django 3.2.18 on 2023-06-08 12:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('add_recipe', '0002_auto_20230419_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='recipe_like', to=settings.AUTH_USER_MODEL),
        ),
    ]