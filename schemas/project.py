from marshmallow import Schema, fields

from utils.functions.not_blank import not_blank
from schemas.page import PageResponseSchema, PageSchema


class PlainProjectResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str(
        validate=not_blank,
    )
    description = fields.Str(
        validate=not_blank,
    )
    start_date = fields.Date()
    end_date = fields.Date()


class ProjectParamsSchema(Schema):
    name = fields.Str(validate=not_blank, required=True)
    description = fields.Str(validate=not_blank, required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=False)


class ProjectQueryParamsSchema(PageSchema):
    name = fields.Str(
        validate=not_blank,
    )
    description = fields.Str(
        validate=not_blank,
    )
    end_date = fields.Date()


class ProjectResponsePaginatedSchema(PageResponseSchema):
    data = fields.List(fields.Nested("PlainProjectResponseSchema"))
