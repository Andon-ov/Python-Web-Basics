from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_only_letters_numbers_and_underscore(value: str):
    for ch in value:
        if not ch.isalnum() or ch == '_':
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_only_letters_numbers_and_underscore,
        )
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    # ▪ The age cannot be below 0.


class Album(models.Model):
    POP = 'Pop Music'
    JAZ = 'Jazz Music'
    R_AND_B = 'R&B Music'
    ROCK = 'Rock Music'
    COUNTRY = 'Country Music'
    DANCE = 'Dance Music'
    HIP_HOP = 'Hip Hop Music'
    OTHER = 'Other'

    GENRE_TYPES = [(x, x) for x in (POP, JAZ, R_AND_B, ROCK, COUNTRY, DANCE, HIP_HOP, OTHER,)]

    ALBUM_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    PRICE_MIN_VALUE = 0.0

    album_name = models.CharField(
        max_length=ALBUM_MAX_LEN,
        unique=True,
    )
    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GENRE_TYPES

    )
    description = models.TextField(
        blank=True,
        null=True
    )
    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    # ▪ The number of decimal places of the price should not be specified in the database.
