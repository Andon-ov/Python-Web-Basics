from django.contrib.auth.models import User
from django.db import models

from petstagram.core.models_mixin import StrFormFieldMixin
from petstagram.photos.models import Photo


class PhotoComment(StrFormFieldMixin, models.Model):
    str_fields = ('publication_date_and_time', 'text')
    TEXT_MAX_LEN = 300

    text = models.CharField(
        max_length=TEXT_MAX_LEN,
        null=False,
        blank=False
    )
    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True
    )
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True
    )


class PhotoLike(StrFormFieldMixin, models.Model):
    str_fields = ('photo',)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True
    )

    # user = models.ForeignKey(
    #     User,
    #     on_delete=
    # )
