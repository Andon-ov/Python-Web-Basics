from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Book(models.Model):
    TITLE_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
