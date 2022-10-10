from django.db import models


class Measure(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Measure, on_delete=models.DO_NOTHING)
    base = models.ForeignKey(to='Recipe', related_name='base', on_delete=models.DO_NOTHING, null=True, default=None,
                             blank=True)

    def __str__(self):
        return f"{self.name} {self.quantity} {self.unit}"


class Recipe(models.Model):
    SOUP = 'Soup'
    SALAD = 'Salad'
    APPETIZER = 'Appetizer'
    PASTA = 'Pasta'
    MAIN_DISH = 'Main Dish'
    PIZZA = 'Pizza'
    DESSERT = 'Dessert'
    BASE = 'Base'

    FOOD_CHOICES = [(x, x) for x in (SOUP, SALAD, APPETIZER, PASTA, MAIN_DISH, PIZZA, DESSERT, BASE)]
    FOOD_TYPE_MAX_LEN = max((len(x) for (x, _) in FOOD_CHOICES))

    title = models.CharField(max_length=30, unique=True)
    food_type = models.CharField(max_length=FOOD_TYPE_MAX_LEN, choices=FOOD_CHOICES)
    image_url = models.URLField()
    instructions = models.TextField()

    ingredient = models.ManyToManyField(to=Ingredient, related_name='ingredient')

    # time = models.IntegerField()

    def get_ingredients(self):
        return ", ".join([str(i) for i in self.ingredient.all()])

    def __str__(self):
        return f"{self.title} {self.ingredient}"
