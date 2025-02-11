from marshmallow import Schema, fields, validate
from utils.validations.messages.schemas import INVALID_ID, INVALID_SIZE, REQUIRED_FIELD


class UserTaskResponseSchema(Schema):
    id = fields.Int()
    team_user_id = fields.Int()
    task_id = fields.Int()


class UserTaskParamsSchema(Schema):
    team_user_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error=INVALID_ID.format("team_user")),
    )
    task_id = fields.Int(
        required=True, validate=validate.Range(min=1, error=INVALID_ID.format("task"))
    )


class UserTaskQueryParamsSchema(Schema):
    team_user_id = fields.Int()
    task_id = fields.Int()
