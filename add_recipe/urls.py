from django.urls import path
from .views import AddRecipe, All_Recipes


urlpatterns = [
    path("add/", AddRecipe.as_view(), name='add_recipe'),
    path("", All_Recipes.as_view(), name="all_recipes"),
]