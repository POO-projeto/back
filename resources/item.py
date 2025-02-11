from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.item import ItemQueryParamsSchema, ItemResponseSchema, ItemParamsSchema
from models.item import Item
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present

blp = Blueprint("Items", __name__, description="Operations on Items")


@blp.route("/item")
class ItemList(ResourceModel):
    @is_logged_in
    @blp.arguments(ItemQueryParamsSchema, location="query")
    @blp.response(200, ItemResponseSchema(many=True))
    def get(self, args):
        query = filter_query(Item, args)
        items = query.all()
        return items

    @is_logged_in
    @handle_exceptions
    @blp.arguments(ItemParamsSchema)
    @blp.response(201)
    def post(self, new_item_data):
        new_item = Item(**new_item_data)
        self.save_data(new_item)
        return {"message": "Item criado com sucesso"}, 201


@blp.route("/item/<int:id>")
class ItemId(ResourceModel):
    @is_logged_in
    @blp.response(200, ItemResponseSchema)
    def get(self, id):
        item = Item.query.get_or_404(id)
        return item, 200

    @is_logged_in
    @handle_exceptions
    @blp.arguments(ItemQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        item = Item.query.get_or_404(id)
        update_if_present(item, args)
        self.save_data(item)
        return {"message": "Item editado com sucesso"}, 200

    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        item = Item.query.get_or_404(id)
        self.delete_data(item)
        return {"message": "Item deletado com sucesso"}, 200
