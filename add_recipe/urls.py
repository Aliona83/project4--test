from django.urls import path
from .views import AddRecipe, All_Recipes, Each_recipe_details, deleteRecipe, updateRecipe, AddLikes, DisLike


urlpatterns = [
    path("add/", AddRecipe.as_view(), name='add_recipe'),
    path("", All_Recipes.as_view(), name="all_recipes"),
    path("post/<int:pk>/like", AddLikes().as_view(), name="like"),
    path("post/<int:pk>/dislike", DisLikes().as_view(), name="dislike"),
    path("<slug:pk>/", Each_recipe_details.as_view(), name="recipe_details"),
    path("delete/<int:pk>/", deleteRecipe.as_view(), name="delete_recipe"),
    path("update/<int:pk>/", updateRecipe.as_view(), name="update_recipe"),
]
