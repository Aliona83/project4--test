from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import recipes
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RecipeForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages


def likeView(request, pk, *args, **kwargs):
    """
    Like Recipes
    """
    post = get_object_or_404(recipes, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse("all_recipes"))


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        recipe_object = data['object_list'].first()
        if recipe_object is not None:
            pk = recipe_object.id
        likes_connected = get_object_or_404(recipes, id=pk)
        likes_list = likes_connected.likes.all()
        liked = False
        if likes_list.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


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

    def get_success_url(self):
        return reverse("all_recipes")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user

        if form.is_valid():
            messages.success(self.request, "You successfuly add new recipe")
            super().form_valid(form)
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self, request, "Failed ")


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
    success_message = 'You deleted  recipe successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user

        if form.is_valid():
            messages.success(self.request, "You successfully update your recipe")
            super().form_valid(form)
