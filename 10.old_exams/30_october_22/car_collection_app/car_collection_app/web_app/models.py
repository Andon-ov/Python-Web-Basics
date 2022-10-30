from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def year_is_between_1980_and_2049_validator(year):
    if year > 2049 or year < 1980:
        raise ValidationError('Year must be between 1980 and 2049')


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 10
    USERNAME_MAX_LENGTH_ERROR_MESSAGE = 'The username must be a minimum of 2 chars'

    AGE_MIN_VALUE = 18

    PASSWORD_MAX_LENGTH = 30

    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH, message=USERNAME_MAX_LENGTH_ERROR_MESSAGE),

        ),
        blank=False,
        null=False,
    )

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
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        verbose_name='Last Name'
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )

    @property
    def name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return None


class Car(models.Model):
    TYPE_MAX_LENGTH = 10

    MODEL_MIN_LENGTH = 2
    MODEL_MAX_LENGTH = 20

    PRICE_MIN_VALUE = 1

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPE_CHOICES = [(x, x) for x in (SPORTS_CAR,
                                         PICKUP,
                                         CROSSOVER,
                                         MINIBUS,
                                         OTHER)]
    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=CAR_TYPE_CHOICES,
        blank=False,
        null=False,
    )
    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=(
            MinLengthValidator(MODEL_MIN_LENGTH),
        ),

        blank=False,
        null=False,
    )
    year = models.IntegerField(
        validators=(
            year_is_between_1980_and_2049_validator,
        ),
        blank=False,
        null=False,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL'
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
        blank=False,
        null=False,
    )
