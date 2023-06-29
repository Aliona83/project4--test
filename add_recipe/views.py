from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import recipes
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RecipeForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from allauth.account.views import LogoutView


class All_Recipes(LoginRequiredMixin, ListView):
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        recipe = data['recipe']
        recipe.is_liked = recipe.likes.filter(id=self.request.user.id).exists()
        return data


def likeView(request, recipe_pk):
    """
    Like  each recipe
    """
    recipe = get_object_or_404(recipes, id=recipe_pk)
    user = request.user

    if recipe.likes.filter(id=user.id).exists():
        recipe.likes.remove(user)
    else:
        recipe.likes.add(user)

    return HttpResponseRedirect(
        (reverse('recipe_details',  kwargs={'pk': recipe_pk})))


def like_recipe(request, recipe_pk):
    recipe = get_object_or_404(recipes, id=recipe_pk)
    recipe.likes.add(request.user)
    return HttpResponseRedirect(
        (reverse('recipe_details', kwargs={'pk': recipe_pk})))


def unlike_recipe(request, recipe_pk):
    """
    Unlike recipe
    """
    recipe = get_object_or_404(recipes, id=recipe_pk)
    recipe.likes.remove(request.user)
    return HttpResponseRedirect(
        (reverse('recipe_details', kwargs={'pk': recipe_pk})))


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Create recipe view
    """
    template_name = 'add_recipe/add_recipe.html'
    model = recipes
    form_class = RecipeForm
    success_url = '/add_recipe/'
    success_message = 'You add new  recipe successfully'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user

        if form.is_valid():
            messages.success(self.request, 'You add new  recipe successfully')
            super().form_valid(form)
            return HttpResponseRedirect(reverse("all_recipes"))
        else:
            return self.form_invalid(forms)


class deleteRecipe(LoginRequiredMixin, DeleteView,):
    """
    Delete recipe
    """
    model = recipes
    success_url = '/add_recipe/'
    template_name = 'add_recipe/recipes_confirm_delete.html'
    success_message = 'You deleted  recipe successfully'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(deleteRecipe, self).delete(request, *args, **kwargs)


class updateRecipe(LoginRequiredMixin, UpdateView):
    """
    Update recipe
    """
    model = recipes
    success_url = '/add_recipe/'
    form_class = RecipeForm
    template_name = 'add_recipe/update_recipe.html'
    success_message = 'You update  recipe successfully'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'You update  recipe successfully')
        super().form_valid(form)
        return HttpResponseRedirect(reverse('all_recipes'))
