from django.contrib import admin

from cook_book.recipes.models import Recipe, Ingredient, Measure


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'food_type', 'get_ingredients')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
    # list_display = ('measure',)


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    pass

# @admin.register(Quantity)
# class QuantityAdmin(admin.ModelAdmin):
#     pass
