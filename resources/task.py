from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.task import TaskQueryParamsSchema, TaskResponseSchema, TaskParamsSchema
from models.task import Task
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present
from utils.functions.add_nested_params import (
    add_nested_params,
    add_nested_params_to_list,
)

blp = Blueprint("Tasks", __name__, description="Operations on tasks")


@blp.route("/task")
class TaskList(ResourceModel):
    @is_logged_in
    @blp.arguments(TaskQueryParamsSchema, location="query")
    @blp.response(200, TaskResponseSchema(many=True))
    def get(self, args):
        query = filter_query(Task, args)
        tasks = query.all()
        return add_nested_params_to_list(tasks, ["groups", "team_users"])

    @is_logged_in
    @handle_exceptions
    @blp.arguments(TaskParamsSchema)
    @blp.response(201)
    def post(self, new_task_data):
        new_task = Task(**new_task_data)
        self.save_data(new_task)
        return {"message": "Task criada com sucesso"}, 201


@blp.route("/task/<int:id>")
class TaskId(ResourceModel):
    @is_logged_in
    @blp.response(200, TaskResponseSchema)
    def get(self, id):
        task = Task.query.get_or_404(id)
        task_dict = add_nested_params(task, ["groups", "team_users"])
        return task_dict, 200

    @is_logged_in
    @handle_exceptions
    @blp.arguments(TaskQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        task = Task.query.get_or_404(id)
        update_if_present(task, args)
        self.save_data(task)
        return {"message": "Task editada com sucesso"}, 200

    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        task = Task.query.get_or_404(id)
        self.delete_data(task)
        return {"message": "Task deletada com sucesso"}, 200
