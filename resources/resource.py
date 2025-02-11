from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from config import db


class ResourceModel(MethodView):
    def save_data(self, obj):
        try:
            db.session.add(obj)
            db.session.commit()
        except SQLAlchemyError as error:
            raise SQLAlchemyError(f"Erro ao salvar dados. Código: {error}")

    def delete_data(self, obj):
        try:
            db.session.delete(obj)
            db.session.commit()
        except SQLAlchemyError as error:
            raise SQLAlchemyError(f"Erro ao deletar dados. Código {error}")
