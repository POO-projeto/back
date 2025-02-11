from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.user_task import (
    UserTaskQueryParamsSchema,
    UserTaskResponseSchema,
    UserTaskParamsSchema,
)
from models.user_task import UserTask
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query

blp = Blueprint("UserTasks", __name__, description="Operations on Users")


@blp.route("/user_task")
class UserTaskList(ResourceModel):
    @is_logged_in
    @blp.arguments(UserTaskQueryParamsSchema, location="query")
    @blp.response(200, UserTaskResponseSchema(many=True))
    def get(self, args):
        query = filter_query(UserTask, args)
        users = query.all()
        return users

    @is_logged_in
    @handle_exceptions
    @blp.arguments(UserTaskParamsSchema)
    @blp.response(201)
    def post(self, new_user_data):
        new_user = UserTask(**new_user_data)
        self.save_data(new_user)
        return {"message": "Usuário adicionado à Task com sucesso"}, 201


@blp.route("/user_task/<int:id>")
class UserTaskId(ResourceModel):
    @is_logged_in
    @blp.response(200, UserTaskResponseSchema)
    def get(self, id):
        user_task = UserTask.query.get_or_404(id)
        return user_task, 200

    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        user = UserTask.query.get_or_404(id)
        self.delete_data(user)
        return {"message": "Usuário removido da Task com sucesso"}, 200
