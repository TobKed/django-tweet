from django.core.exceptions import ValidationError


def validate_content(value):
    if value == "another bad word again":
        raise ValidationError("Cannot be another bad word again")
    return value
