from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import recipes
from .forms import RecipeForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages 


class All_Recipes(ListView):
    """
    View all recipes
    """

    template_name = "add_recipe/all_recipes.html"
    model = recipes
    context_object_name = "all_recipes"
    paginate_by = 2
    queryset = recipes.objects.all()

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


class Each_recipe_details(LoginRequiredMixin, DetailView):
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
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class deleteRecipe(LoginRequiredMixin, DeleteView,):
    model = recipes
    success_url = '/add_recipe/'
    template_name = 'add_recipe/recipes_confirm_delete.html'
    success_message = 'Recipe deleted successfully'
     
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(deleteRecipe, self).delete(request, *args, **kwargs)


class updateRecipe(LoginRequiredMixin, UpdateView):
    model = recipes
    success_url = '/add_recipe/'
    form_class = RecipeForm
    template_name = 'add_recipe/update_recipe.html'


