from django.views.generic import CreateView
from .modules import recipes
from .forms import RecipeForm


# Create your views here.
class AddRecipe(CreateView):
    template_name = 'add_recipe/add_recipe.html'
    model = recipes
    success_url = '/add_recipe/'

    def form_valid(sel, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)