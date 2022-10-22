from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
        blank=False,
        null=False,
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    @property
    def name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return None


class GameModel(models.Model):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"
    GAME_TYPE = [(x, x) for x in (
        ACTION,
        ADVENTURE,
        PUZZLE,
        STRATEGY,
        SPORTS,
        BOARD_CARD_GAME,
        OTHER,
    )]

    TITLE_MAX_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15

    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0

    MAX_LEVEL_MIN_VALUE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )
    category = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        choices=GAME_TYPE,
        blank=False,
        null=False,
    )
    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        ),
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )
    max_Level = models.IntegerField(
        validators=(
            MinValueValidator(MAX_LEVEL_MIN_VALUE),
        ),
        blank=True,
        null=True,
    )
    summary = models.TextField(
        blank=True,
        null=True,
    )
