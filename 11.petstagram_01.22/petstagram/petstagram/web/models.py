import datetime


from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.web.validators import validate_only_letters, validate_file_max_size_in_mb

# Create your models here.
class Profile(models.Model):
    # Constants
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"

    GANDER = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    # Същото като долното

    # GANDER_CHOICES = (
    #     ("Male", "Male"),
    #     ("Female", "Female"),
    #     ("Do not show", "Do not show")
    # )

    # Fields
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=(
                                      MinLengthValidator(FIRST_NAME_MIN_LENGTH),
                                      validate_only_letters,

                                  ))
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,
                                 validators=(
                                     MinLengthValidator(LAST_NAME_MIN_LENGTH),
                                     validate_only_letters,

                                 ))

    picture = models.URLField()

    # • Date of birth: day, month, and year of birth.
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,  # не задължителен параметър
        blank=True,  # за да може да се обработва през регистрацията
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max((len(x) for (x, _) in GANDER)),  # Динамична дължина
        # max_length=(15),
        null=True,
        blank=True,
        choices=GANDER,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    # Constants

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    PET_TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    NAME_MAX_LENGTH = 30
    # MIN_DATE = datetime.date(1920, 1, 1)

    # Fields
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        #  unique=True - Това го прави уникално за целия модел
    )
    type = models.CharField(
        max_length=max(len(x) for x, _ in PET_TYPES),
        choices=PET_TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        # validators=(
        #     MinDateValidator(),
        #     MaxDateValidator(),
        # )
    )
    #  One-to-one relations

    #  One-to-many relations
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    #  Many-to-many relations

    #  Properties
    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    #  Methods

    #  dunder methods

    #  Meta
    class Meta:
        unique_together = ('user_profile', 'name')  # Така ги правим да са уникална двойка


# Pet's Photo
# The user must provide the following information when uploading a pet's photo in their profile:
#     • Photo - the maximum size of the photo can be 5MB
#     • Tagged pets - the user should tag at least one of their pets. There is no limit in the number of tagged pets
# The user may provide the following information when uploading a pet's photo in their profile:
#     • Description - a user can write any description about the picture, with no limit of words/chars
# Other:
#     • Date and time of publication - when a picture is created (only), the date and time of publication are automatically generated.
#     • Likes - each picture has 0 likes at the beginning, and no one can change it. The number of likes a picture can collect is unlimited.

class PetPhoto(models.Model):
    MAX_FILE_SIZE_IN_MB = 5

    photo = models.ImageField(
        validators=(
            validate_file_max_size_in_mb,  # (MAX_FILE_SIZE_IN_MB)
        )
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least 1 pet
    )

    description = models.TextField(
        blank=True,
        null=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )
