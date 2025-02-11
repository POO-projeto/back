import jwt
from flask import request, current_app
from models import User
from werkzeug.exceptions import Unauthorized


def get_logged_in_user():

    auth_header = request.headers.get("Authorization", None)
    if not auth_header:
        raise Unauthorized("Token não fornecido.")

    try:
        token = auth_header.split(" ")[1]
        payload = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
        )

        user_email = payload.get("email")
        if not user_email:
            raise Unauthorized("Token inválido, email não encontrado.")
        user = User.query.filter_by(email=user_email).first()
        if not user:
            raise Unauthorized("Usuário não encontrado.")
        return user

    except jwt.ExpiredSignatureError:
        raise Unauthorized("Token expirado. Faça login novamente.")
    except jwt.InvalidTokenError:
        raise Unauthorized("Token inválido. Faça login novamente.")
