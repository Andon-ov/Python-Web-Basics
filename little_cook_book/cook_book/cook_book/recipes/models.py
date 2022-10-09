from django.db import models


class Recipe(models.Model):
    SOUP = 'Soup'
    SALAD = 'Salad'
    APPETIZER = 'Appetizer'
    PASTA = 'Pasta'
    MAIN_DISH = 'Main Dish'
    PIZZA = 'Pizza'
    DESSERT = 'Dessert'

    FOOD_CHOICES = [(x, x) for x in (SOUP, SALAD, APPETIZER, PASTA, MAIN_DISH, PIZZA, DESSERT)]

    TITLE_MAX_LEN = 30
    FOOD_TYPE_MAX_LEN = max((len(x) for (x, _) in FOOD_CHOICES))

    INGREDIENTS_MAX_LEN = 250 # Това искам да е отделлна таблица която да има релация one to one

    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    image_url = models.URLField()

    description = models.TextField()

    food_type = models.CharField(
        max_length=FOOD_TYPE_MAX_LEN,
        choices=FOOD_CHOICES
    )
    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LEN
    )
    # time = models.IntegerField()
    def __str__(self):
        return f'{self.title}'
