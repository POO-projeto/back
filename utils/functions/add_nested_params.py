from utils.functions.nest_item import nest_items
from utils.functions.nest_scholarship import nest_scholarship
from utils.functions.nest_task import nest_tasks
from utils.functions.nest_user import nest_user


def add_nested_params_to_list(objs, params):
    return [add_nested_params(obj, params) for obj in objs]


def add_nested_params(obj, params):
    nest_funcs = {
        "tasks": nest_tasks,
        "items": nest_items,
        "scholarship": nest_scholarship,
        "user": nest_user,
    }
    obj_dict = obj.__dict__.copy()
    for attr in params:
        if attr in nest_funcs:
            obj_dict[attr] = nest_funcs[attr](obj)
    return obj_dict
