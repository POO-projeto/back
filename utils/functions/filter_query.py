from sqlalchemy.orm import class_mapper


def filter_query(model, filter_args):
    query = model.query
    model_attributes = {column.name: column for column in class_mapper(model).columns}
    for key, value in filter_args.items():
        if value is not None and key in model_attributes:
            query = query.filter(model_attributes[key] == value)
    return query
