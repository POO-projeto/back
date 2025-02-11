from marshmallow import Schema, fields, validate
from utils.functions.validate_date import validate_date
from utils.functions.not_blank import not_blank

from schemas.page import PageResponseSchema, PageSchema


class DailyResponseSchema(Schema):
    id = fields.Int()
    date = fields.Date()
    items = fields.List(fields.Nested("ItemResponseSchema"))
    issue = fields.Str(
        validate=not_blank,
    )
    user = fields.Nested("PlainUserResponseSchema")


class DailyUpdateItemsSchema(Schema):
    id = fields.Int()
    description = fields.Str(
        validate=not_blank,
    )


class DailyUpdateSchema(Schema):
    items = fields.List(fields.Nested("DailyUpdateItemsSchema"))
    issue = fields.Str(
        validate=not_blank,
    )


class DailyParamsSchema(Schema):
    date = fields.Str(validate=validate.And(validate_date, not_blank))
    items = fields.List(
        fields.Str(
            validate=not_blank,
        )
    )
    issue = fields.Str(
        validate=not_blank,
    )


class DailyQueryParamsSchema(PageSchema):
    user_id = fields.Int()
    date = fields.Date()


class DailyResponsePaginatedSchema(PageResponseSchema):
    data = fields.List(fields.Nested("DailyResponseSchema"))
