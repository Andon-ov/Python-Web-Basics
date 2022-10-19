from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def only_letters_numbers_and_underscore_validator(value: str):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            only_letters_numbers_and_underscore_validator,
        ),
        blank=False,
        null=False,
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    POP_MUSIC = "Pop Music"
    JAZ_MUSIC = "Jazz Music"
    R_AND_B_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    GENRE_CHOICE = [(x, x) for x in (POP_MUSIC,
                                     JAZ_MUSIC,
                                     R_AND_B_MUSIC,
                                     ROCK_MUSIC,
                                     COUNTRY_MUSIC,
                                     DANCE_MUSIC,
                                     HIP_HOP_MUSIC,
                                     OTHER)]

    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    PRICE_MIN_VALUE = 0.0

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
        blank=False,
        null=False,
    )
    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
        blank=False,
        null=False,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GENRE_CHOICE,
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )
    # The number of decimal places of the price should not be specified in the database.
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.album_name} {self.artist}'
