from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

"""
Filter recipes
"""

MEAL_TYPES = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner')
)


class recipes(models.Model):
    """
    A model to create and manage recipes
    """
    user = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False, default='')
    image = ResizedImageField(size=[400, None], quality=75, upload_to='add_recipe/', force_format='WEBP', blank=False, null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default='breakfast')
    posted_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_date']

