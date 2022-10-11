from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    PET_NAME_MAX_LEN = 30
    name = models.CharField(
        max_length=PET_NAME_MAX_LEN,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(

        null=False,
        blank=False,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Create/Update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(
                f'{self.id}-{self.name}'
            )
        # Update
        return super().save(*args, **kwargs)


