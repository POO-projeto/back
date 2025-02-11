from functools import wraps
from sqlalchemy.exc import SQLAlchemyError


def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            return {"message": f"Erro de banco de dados: {e}"}, 500

    return wrapper
