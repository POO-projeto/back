from marshmallow import ValidationError
from datetime import date


def validate_date(d):
    if d > str(date.today()):
        raise ValidationError("A data não pode ser no futuro.")
