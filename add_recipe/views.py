from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import recipes
from .forms import RecipeForm
from django.db.models import Q


class All_Recipes(ListView):
    """
    View all recipes
    """
    template_name = "add_recipe/all_recipes.html"
    model = recipes
    context_object_name = "all_recipes"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(meal_type__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes


class Each_recipe_details(DetailView):
    """
    Details for each recipe
    """
    template_name = 'add_recipe/recipe_details.html'
    model = recipes
    context_object_name = "recipe"


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Create recipe view
    """
    template_name = 'add_recipe/add_recipe.html'
    model = recipes
    form_class = RecipeForm
    success_url = '/add_recipe/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class deleteRecipe(DeleteView):
    model = recipes
    success_url = '/add_recipe/'
   
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete, self).form_valid(form)


class updateRecipe(UpdateView):
    model = recipes
    success_url = '/add_recipe/'
    form_class = RecipeForm()
    template_name = 'add_recipe/update_recipe.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)