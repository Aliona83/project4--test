from django.contrib import admin
from .models import recipes
# Register your models here.


@admin.register(recipes)
class RecipeAdmin(admin.ModelAdmin):
    
    list_display = (
        'title',
        'meal_type',
        'instructions',
        'ingredients',
        'image'
    )
    list_filter = ('meal_type',)

