from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = "Ensure this value contains only letters."


@deconstructible
class MaxFileSizeImMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.file.size > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_messages())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_messages(self):
        return f"Max file size is {self.max_size:.2f} MB"


def only_letters_validator(value: str):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)