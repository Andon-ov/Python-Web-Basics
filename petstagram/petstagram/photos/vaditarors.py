from django.core.exceptions import ValidationError

from petstagram.core.utils import megabytes_to_bytes


def validate_file_less_then_5mb(file_obj):
    filesize = file_obj.file.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f"Max file size is {megabyte_limit}MB")
