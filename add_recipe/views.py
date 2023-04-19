from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .modules import recipes
from .forms import RecipeForm


# Create your views here.
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