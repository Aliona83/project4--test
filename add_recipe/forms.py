from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import recipes


class RecipeForm(forms.ModelForm):
    class Meta:
        model = recipes
        exclude = ('likes',)
        fields = ['title', 'description', 'ingredients', 'instructions',
                  'image', 'image_alt', 'meal_type']

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widget = {
            'descriptions': forms.Textarea(attrs={'rows': 5}),
        }

        labels = {
            'title': 'Recipe Title',
            'descriptions': 'Descriptions',
            'ingredients': 'Recipe Ingredients',
            'instructions': 'Recipe Instructions',
            'image': 'Recipe Image',
            'image_alt': 'Describe Image',
            'meal_type': 'Meal Type'
        }
