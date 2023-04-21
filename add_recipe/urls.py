from django.urls import path
from .views import AddRecipe, All_Recipes


urlpatterns = [
    path("", AddRecipe.as_view(), name='add_recipe'),
    path("all_recipes/", All_Recipes.as_view(), name="all_Recipes"),
]