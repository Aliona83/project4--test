from django.urls import path
from . import views
from .views import AddRecipe, All_Recipes, Each_recipe_details, deleteRecipe
from .views import updateRecipe, like_recipe, unlike_recipe, likeView

urlpatterns = [
    path("add/", AddRecipe.as_view(), name='add_recipe'),
    path("", All_Recipes.as_view(), name="all_recipes"),
    path("<slug:pk>/", Each_recipe_details.as_view(), name="recipe_details"),
    path("delete/<int:pk>/", deleteRecipe.as_view(), name="delete_recipe"),
    path("update/<slug:pk>/", updateRecipe.as_view(), name="update_recipe"),
    path('like_recipe/<int:recipe_pk>/', views.like_recipe, name='like_recipe'),
    path('unlike_recipe/<int:recipe_pk>/', views.unlike_recipe, name='unlike_recipe'),
]
