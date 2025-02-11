from flask_smorest import Blueprint

from models.project import Project
from resources.resource import ResourceModel
from schemas.page import Page
from schemas.project import (
    PlainProjectResponseSchema,
    ProjectParamsSchema,
    ProjectQueryParamsSchema,
    ProjectResponsePaginatedSchema,
)
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present

blp = Blueprint("Projects", __name__, description="Operations on Projects")


@blp.route("/project")
class ProjectList(ResourceModel):
    @is_logged_in
    @blp.arguments(ProjectQueryParamsSchema, location="query")
    @blp.response(200, ProjectResponsePaginatedSchema)
    def get(self, args):
        page = args.get("page")
        per_page = args.get("per_page")
        query = filter_query(Project, args)
        projects = query.order_by(Project.id.desc()).all()
        page_response = Page(page=page, per_page=per_page, data=projects)
        return page_response.to_json()

    @is_logged_in
    @handle_exceptions
    @blp.arguments(ProjectParamsSchema)
    @blp.response(201)
    def post(self, new_project_data):
        if (
            new_project_data.get("end_date")
            and new_project_data["start_date"] > new_project_data["end_date"]
        ):
            return {
                "message": "Não é possível criar um projeto com data final menor que a inicial"
            }, 500
        new_project = Project(**new_project_data)
        self.save_data(new_project)
        return {"message": "Projeto criado com sucesso"}, 201


@blp.route("/project/<int:id>")
class ProjectId(ResourceModel):
    @is_logged_in
    @blp.response(200, PlainProjectResponseSchema)
    def get(self, id):
        project = Project.query.get_or_404(id)
        return project, 200

    @is_logged_in
    @handle_exceptions
    @blp.arguments(ProjectQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        project = Project.query.get_or_404(id)
        if args.get("end_date") and project.start_date > args["end_date"]:
            return {
                "message": "Não é possível mudar a data final do projeto para uma menor que a inicial"
            }, 500
        update_if_present(project, args)
        self.save_data(project)
        return {"message": "Projeto editado com sucesso"}, 200

    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        project = Project.query.get_or_404(id)
        self.delete_data(project)
        return {"message": "Projeto deletado com sucesso"}, 200
