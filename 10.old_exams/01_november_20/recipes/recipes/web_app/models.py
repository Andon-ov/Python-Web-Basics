from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 30
    INGREDIENTS_MAX_LENGTH = 250

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        blank=False,
        null=False
    )
    image_url = models.URLField(
        verbose_name='Image URL',
        blank=False,
        null=False
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LENGTH,
        blank=False,
        null=False
    )
    time = models.IntegerField(
        verbose_name='Time(Minutes)',
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('pk',)
