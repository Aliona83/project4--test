from django.urls import path
from .views import AddRecipe, All_Recipes, Each_recipe_details, deleteRecipe


urlpatterns = [
    path("add/", AddRecipe.as_view(), name='add_recipe'),
    path("", All_Recipes.as_view(), name="all_recipes"),
    path("<slug:pk>/", Each_recipe_details.as_view(), name="recipe_details"),
    path("delete/<slug:pk>/", deleteRecipe.as_view(), name="delete_recipe"),
]