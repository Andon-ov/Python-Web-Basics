from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProfileModel(models.Model):
    email = models.EmailField()
    age = models.IntegerField(
        validators=(
            MinValueValidator(12),
            # The age cannot be below 12
        ),
    )
    password = models.CharField(
        max_length=30,
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class GameModel(models.Model):
    CATEGORY_CHOICES = (
        ("ACTION", "Action"),
        ("ADVENTURE", "Adventure"),
        ("PUZZLE", "Puzzle"),
        ("STRATEGY", "Strategy"),
        ("SPORTS", "Sports"),
        ("BORD/CARD GAME", "Board/Card Game"),
        ("OTHER", "Other"),
    )

    title = models.CharField(
        max_length=30,
        unique=True,
        # ▪ All game titles must be unique.
    )
    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES,

    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1)
            , MaxValueValidator(5.0),
        ),
        # ▪ The rating can be between 0.1 and 5.0 (both inclusive).
    )
    max_level = models.IntegerField(
        validators=(
            MinValueValidator(1),
        ),
        # ▪ The max level cannot be below 1.
        blank=True,
        null=True,
    )
    image_url = models.URLField()
    summary = models.TextField(
        null=True,
        blank=True
    )

# Note: the validations will be examined only by the user side, not the admin side.
