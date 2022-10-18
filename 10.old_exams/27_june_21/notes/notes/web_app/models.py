from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH
    )
    age = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Note(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    image_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.title
