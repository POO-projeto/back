from models.item import Item


def nest_items(obj):
    return [Item.query.get(item_obj.id) for item_obj in obj.items]
