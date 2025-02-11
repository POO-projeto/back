from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import (
    INVALID_NAME,
    INVALID_DESCRIPTION,
    INVALID_ID,
)


class PlainTaskResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    status_id = fields.Int()
    priority_id = fields.Int()
    difficulty_id = fields.Int()
    task_type_id = fields.Int()


class TaskResponseSchema(PlainTaskResponseSchema):
    user = fields.List(fields.Nested("PlainUserResponseSchema"))


class TaskParamsSchema(Schema):
    name = fields.Str(
        required=True, validate=validate.Length(min=1, max=100, error=INVALID_NAME)
    )
    description = fields.Str(
        required=True, validate=validate.Length(min=1, error=INVALID_DESCRIPTION)
    )
    status_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("'Status'")),
    )
    priority_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("'Priority'")),
    )
    difficulty_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("'Difficulty'")),
    )
    task_type_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("'Task Type'")),
    )


class TaskQueryParamsSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    status_id = fields.Int()
    priority_id = fields.Int()
    difficulty_id = fields.Int()
    task_type_id = fields.Int()
