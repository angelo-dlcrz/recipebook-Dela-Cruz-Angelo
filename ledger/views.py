from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

def recipe_list(request):
    recipe = Recipe.objects.all()
    ctx = {
        'recipe': recipe
    }
    return render(request, 'recipe_list.html', ctx)

def recipes(request, id):
    ctx = {
        'recipe', Recipe.objects.get(id=id)
    }
    return render(request, 'recipe.html', ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
