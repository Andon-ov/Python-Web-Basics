from django.core.exceptions import ValidationError


def validate_only_letters(value: str):
    if not value.isalpha():
        raise ValidationError('Name must contain only letters')


def validate_file_max_size_in_mb(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            # raise ValidationError("Max file size is %sMB" % str(max_size))
            raise ValidationError(f"Max file size is {max_size}MB")

    return validate

# @deconstructible
# class MinDateValidator:
#     def __init__(self, min_date):
#         self.min_date = min_date
#
#     def __ceil__(self, value):
#         if value < self.min_date:
#             raise ValidationError(f'Date must be grater then {self.min_date} ')
#
#
# @deconstructible
# class MaxDateValidator:
#     def __init__(self, max_date):
#         self.max_date = max_date
#
#     def __ceil__(self, value):
#         if value > self.max_date:
#             raise ValidationError(f'Date must be earlier then {self.max_date} ')
