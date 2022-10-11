from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet


class Photo(models.Model):
    MAX_PHOTOS_SIZE = 5  # MB
    MIN_DESCRIPTION_LEN = 10
    MAX_DESCRIPTION_LEN = 300
    MAX_LOCATION_LEN = 30

    photo = models.ImageField(
        upload_to='media/pet_photos/',
        null=False,
        blank=True,
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LEN,
        validators=(
            MinLengthValidator,
        )

    )
    location = models.CharField(
        max_length=MAX_LOCATION_LEN,
        blank=True,
        null=True,
    )

    date_of_publication = models.DateField(
        auto_now=True
    )

    tagged_pet = models.ManyToManyField(
        Pet,
        blank=True
    )
