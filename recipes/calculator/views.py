from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from pprint import pprint



DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },


}

def show_recipe(request, recipe_name):
    recipe = DATA.get(recipe_name)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:

    servings = request.GET.get('servings', 2)
    if servings:
        recipe = {ingredient: amount * int(servings) for ingredient, amount in recipe.items()}
    context = {
        'recipe': recipe

}
    return render(request, 'calculator/index.html', context)
