from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import recipes
from .forms import RecipeForm


class All_Recipes(ListView):
    """
    View all recipes
    """
    template_name = "add_recipe/all_recipes.html"
    model = recipes
    context_object_name = "all_recipes"


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Create recipe view
    """
    template_name = 'add_recipe/add_recipe.html'
    model = recipes
    form_class = RecipeForm
    success_url = '/add_recipe/'

    def form_valid(sel, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)