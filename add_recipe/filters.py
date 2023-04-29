import django_filters
from . models import recipes


class recipeFilter(django_filters.FilterSet):

    class Meta:
        model = recipes
        fields = ['meal_type']
        