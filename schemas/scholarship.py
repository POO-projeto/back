from marshmallow import Schema, fields, validate


class PlainScholarShipResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
