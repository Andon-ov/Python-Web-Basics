from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.web_app.validators import only_letters_validator, MaxFileSizeImMbValidator


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    BUDGET_MIN_VALUE = 0
    BUDGET_DEFAULT_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'
    # DEFAULT_IMAGE = 'user.png'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            only_letters_validator,
        ),
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            only_letters_validator,
        ),
        blank=False,
        null=False,
    )
    budget = models.FloatField(
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
        blank=False,
        null=False,
        default=BUDGET_DEFAULT_VALUE,
    )
    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        # default=DEFAULT_IMAGE,
        blank=True,
        null=True,
        validators=(
            MaxFileSizeImMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        blank=False,
        null=False,
    )
    expense_image = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.title} {self.price}'

    class Meta:
        ordering = ('title', 'price')
