from marshmallow import ValidationError


def not_blank(value):
    if isinstance(value, str) and len(value.strip()) == 0:
        raise ValidationError("O campo não pode conter apenas espaços em branco")
