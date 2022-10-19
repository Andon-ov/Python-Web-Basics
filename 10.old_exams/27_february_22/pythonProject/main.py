def only_letters_numbers_and_underscore_validator(value: str):
    for ch in value:
        if not ch.isalpha() and not ch.isdigit() and ch != '_':
            print("error")


only_letters_numbers_and_underscore_validator('Proba1_ ')
