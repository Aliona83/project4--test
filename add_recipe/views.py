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
    success_message = 'You add new recipe'
    
    def get_success_url(self):
        return reverse("all_recipes")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    
    def form_valid(self, form):
        form.instance.user = self.request.user

        if form.is_valid():
            messages.success(self.request, "You add new recipe")
            super().form_valid(form)
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self, request, "Failed ")
        

class deleteRecipe(LoginRequiredMixin, DeleteView,):
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
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self, request, "Failed ")


class AddLikes(LoginRequiredMixin, CreateView):
    template_name = 'add_recipe/add_recipe.html'
    model = recipes
    
    def post(self, request, pk, *args, **kwargs):
        post = recipes.objects.get(pk=pk)
       
        is_dislike = False

        for dislike in post.dislikes.all():
            if dislikes == request.user:
                is_dislike = True  
            break
        is_like = False

        for like in post.likes.all():
            if likes == request.user:
                is_like = True  
            break

        if is_dislike:
            post.dislike.remove(request.user)
        if not is_like:
            post.likes.add(request.user)
        
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class DisLike(LoginRequiredMixin, CreateView):
    def post(self, request, pk, *args, **kwargs):
        post = recipes.objects.get(pk=pk)
       
        is_like = False

        for like in post.likes.all():
            if likes == request.user:
                is_like = True  
            break
        if is_like:
            post.likes.remove(request.user)
   
            is_dislike = False

        for dislike in post.dislikes.all():
            if dislikes == request.user:
                is_dislike = True  
            break
         
        if not is_dislike:
            post.dislikes.add(request.user)  
        if is_dislike:
            post.dislike.remove(request.user)  

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)