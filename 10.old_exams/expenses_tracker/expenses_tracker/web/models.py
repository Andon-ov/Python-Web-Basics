from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.web.validators import validate_only_letters, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )
    # It should have at least 2 characters and maximum - 15 characters.
    # The name should consist only of letters. Otherwise, raise ValidationError with the message: "Ensure this value contains only letters."

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )
    # It should have at least 2 characters and maximum - 15 characters.
    # The name should consist only of letters. Otherwise, raise ValidationError with the message: "Ensure this value contains only letters."

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(MinValueValidator(BUDGET_MIN_VALUE),
                    ),
    )
    # The budget should not be below 0, when created or edited.

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    # Image field, optional(null=True,blank=True,). The picture is user.png (located in the resources) by default; if no image is uploaded)
    # The max size limit is 5MB (inclusive). Otherwise, raise ValidationError with the message: "Max file size is 5.00 MB"


class Expense(models.Model):
    TITLE_MAX_LEN = 30
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ('title', 'price')