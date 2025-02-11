from flask import g
from flask_smorest import Blueprint

from models.item import Item
from models.user import User
from resources.resource import ResourceModel
from schemas.daily import (
    DailyQueryParamsSchema,
    DailyResponsePaginatedSchema,
    DailyResponseSchema,
    DailyParamsSchema,
    DailyUpdateSchema,
)
from models.daily import Daily
from schemas.page import Page
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present
from utils.functions.add_nested_params import (
    add_nested_params,
    add_nested_params_to_list,
)
from utils.functions.date_filter import apply_date_filter

blp = Blueprint("Dailies", __name__, description="Operations on Dailies")


@blp.route("/daily")
class DailyList(ResourceModel):
    @is_logged_in
    @blp.arguments(DailyQueryParamsSchema, location="query")
    @blp.response(200, DailyResponsePaginatedSchema)
    def get(self, args):
        filter_by = args.get("filterBy")
        order_by = args.get("orderBy", "desc")
        user_id = args.get("user_id")
        page = args.get("page")
        per_page = args.get("per_page")
        query = filter_query(Daily, args)
        if user_id:
            query = query.join(User).filter(
                User.id == user_id, Daily.user_id == User.id
            )
        query = apply_date_filter(query, filter_by, args)
        query = query.order_by(Daily.date.desc())
        dailies = query.all()
        dailies = add_nested_params_to_list(dailies, ["items", "user"])
        page_response = Page(page=page, per_page=per_page, data=dailies)
        return page_response.to_json()

    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyParamsSchema)
    @blp.response(201)
    def post(self, new_daily_data):
        id = g.user["id"]
        items = new_daily_data.pop("items")
        if Daily.query.filter_by(date=new_daily_data["date"], user_id=id).first():
            return {"message": "Esse usuário já fez uma daily hoje"}, 409
        new_daily = Daily(**{**new_daily_data, "user_id": id})
        self.save_data(new_daily)
        for item in items:
            new_item = Item(**{"description": item, "daily_id": new_daily.id})
            self.save_data(new_item)
        return {"message": "Daily criada com sucesso"}, 201


@blp.route("/daily/<int:id>")
class DailyId(ResourceModel):
    @is_logged_in
    @blp.response(200, DailyResponseSchema)
    def get(self, id):
        daily = Daily.query.get_or_404(id)
        daily_dict = add_nested_params(daily, ["items", "user"])
        return daily_dict, 200

    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyUpdateSchema)
    def put(self, args, id):
        daily = Daily.query.get_or_404(id)
        ids = list(map(lambda x: x.id, daily.items))
        items_to_update = []
        for item in args["items"]:
            if item["id"] not in ids:
                return {
                    "message": f"Item de id {item["id"]} não encontrado nessa daily"
                }, 404
            item_to_update = Item.query.get_or_404(item["id"])
            items_to_update.append(item_to_update)
        for item in items_to_update:
            new_item = list(filter(lambda x: x["id"] == item.id, args["items"]))[0]
            update_if_present(item, new_item)
            self.save_data(item)
        daily.issue = args["issue"]
        self.save_data(daily)
        return {"message": "Daily editada com sucesso"}, 200

    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        daily = Daily.query.get_or_404(id)
        update_if_present(daily, args)
        self.save_data(daily)
        return {"message": "Daily editada com sucesso"}, 200

    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        daily = Daily.query.get_or_404(id)
        self.delete_data(daily)
        return {"message": "Daily deletada com sucesso"}, 200
