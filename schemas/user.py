from marshmallow import Schema, fields, validate
from utils.functions.validate_date import validate_date
from schemas.page import PageResponseSchema, PageSchema
from utils.functions.not_blank import not_blank
from utils.validations.messages.schemas import (
    INVALID_EMAIL,
    INVALID_SIZE,
    REQUIRED_FIELD,
)
from schemas.scholarship import PlainScholarShipResponseSchema


class PlainUserResponseSchema(Schema):
    id = fields.Int()
    email = fields.Str(
        validate=not_blank,
    )
    photo = fields.Str(
        validate=not_blank,
    )
    name = fields.Str(
        validate=not_blank,
    )
    birthday = fields.Str(validate=validate.And(not_blank, validate_date))
    github = fields.Str(
        validate=not_blank,
    )
    lattes = fields.Str(
        validate=not_blank,
    )
    telephone = fields.Str(
        validate=not_blank,
    )


class UserResponseSchema(PlainUserResponseSchema):
    scholarship = fields.Nested(PlainScholarShipResponseSchema)


class UserResponsePaginatedSchema(PageResponseSchema):
    data = fields.List(fields.Nested("UserResponseSchema"))


class UserParamsSchema(Schema):
    email = fields.Str(
        required=True,
        validate=validate.And(
            not_blank,
            validate.Length(min=1, max=120, error=INVALID_EMAIL),
            validate.Regexp(
                r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,}(\.\w{2,})?(\.\w{2,})?$",
                error=INVALID_EMAIL,
            ),
        ),
        error_messages=dict(required=REQUIRED_FIELD.format("email")),
    )
    photo = fields.Str(
        required=False,
        validate=validate.And(
            validate.Length(min=1, max=255, error=INVALID_SIZE.format("photo")),
            not_blank,
        ),
    )
    name = fields.Str(
        required=True,
        validate=validate.And(
            validate.Length(min=1, max=100, error=INVALID_SIZE.format("name")),
            not_blank,
        ),
        error_messages=dict(required=REQUIRED_FIELD.format("name")),
    )


class UserQueryParamsSchema(PageSchema):
    email = fields.Str(
        validate=not_blank,
    )
    photo = fields.Str(
        validate=not_blank,
    )
    name = fields.Str(
        validate=not_blank,
    )
    birthday = fields.Str(validate=validate.And(not_blank, validate_date))
    github = fields.Str(
        validate=not_blank,
    )
    lattes = fields.Str(
        validate=not_blank,
    )
    telephone = fields.Str(
        validate=not_blank,
    )
    scholarship_id = fields.Int()
