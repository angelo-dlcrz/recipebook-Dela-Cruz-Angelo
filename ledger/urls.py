from django.urls import path

from .views import index, recipe_list, sinigang, adobo

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/1', sinigang, name='sinigang'),
    path('recipe/2', adobo, name='adobo'),
]

app_name = 'ledger'